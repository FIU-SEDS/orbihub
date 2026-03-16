from PyQt6.QtCore import QThread, pyqtSignal
from orbihub.core.app_manager import install_app
from orbihub.utils.paths import get_apps_dir
from orbihub.utils.logger import logger
import subprocess 
import platform 
import re 

class InstallWorker(QObject): 
    progress = pyqtSignal(100)
    status = pyqtSignal(str) #emits a status message
    finished = pyqtSignal(bool, str) 
    
    def __init__(self, app_id: str, name: str, version: str, repo_url: str):
        super().__init__()
        self.app_id = app_id
        self.name = name
        self.version = version
        self.repo_url = repo_url
    
    def run(self): 
        try: 
            #Step 1: Git  cloning repository
            app_install_path = get_apps_dir() / self.app_id
            
            self.status.emit("Cloning repository...")
            self.progress.emit(5) #showing some progress while cloning 
            
            clone_success = self._git_clone(app_install_path)
            if not clone_success:
                self.finished.emit(False, "Failed to clone repository")
                return 
        
            #Step 2: Creating Virtual Enviornment
            self.status.emit("Creating virtual enviornment...")
            self.progress.emit(50)
            venv_path = app_install_path / "venv"
            subprocess.run(["python", "-m", "venv", str(venv_path)], check=True)
            
            #Step 3: Pip install
            self.status.emit("Installing dependencies...")
            self.progress.emit(75)
            
            if platform.system() == "Windows":
                pip_path = venv_path / "Scripts" / "pip"
            else:
                pip_path = venv_path / "bin" / "pip"
                
            requirements = app_install_path / "requirements.txt"
            if requirements.exists():
                subprocess.run(
                    [str(pip_path), "install", "-r", str(requirements)], check = True
                )
            
            self.progress.emit(100)
            self.status.emit("Installation complete!")
            self.finished.emit(True, "Installation successful")
        
        except subprocess.CalledProcessError as e: 
            self.finished.emit(False, f"Installation failed: {e}")
        except Exception as e: 
            self.finished.emit(False, f"Unexpected error: {e}")
            
    def _git_clone(self, app_install_path: Path) -> bool:
        try: 
            process = subprocess.Popen(
                ["git", "clone", "--progress", self.repo_url, str(app_install_path)]
                stderr=subprocess.PIPE, 
                text = True
            )
            
            for line in process.stderr:
                line = line.strip()
                match = re.search(f"Recieving objects:\s+(\d+)", line)
                if match: 
                    percent = int(match.group(1))
                    #scaling range from 5 - 55
                    scaled = 5 + int(percent * 0.5)
                    self.progress.emit(scaled)
                    
                process.wait()
                return process.returncode == 0
        except Exception as e: 
            logger.error(f"Git clone error: {e}")
            return False
        
        
        

                
            
            
            