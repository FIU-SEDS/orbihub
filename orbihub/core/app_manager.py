from orbihub.utils.paths import get_apps_dir
from orbihub.core.database import add_installed_app, remove_installed_apps
from orbihub.utils.checker import check_python_installed, check_git_installed 
from orbihub.utils.logger import logger
from pathlib import Path
import platform
import subprocess
from typing import Tuple
import shutil 

apps_dir = get_apps_dir()

def install_app(app_id : str, name : str, verison : str, repo_url : str) -> Tuple[bool, str]:
  if not (check_git_installed() and check_python_installed()):
    return (False, "Git or Python not installed")
      
  try:
    #git clone
    app_install_path = get_apps_dir() / app_id
    subprocess.run(["git", "clone", repo_url, str(app_install_path)], check=True)
    # print(f"Repo cloned to {apps_dir}")
    logger.info(f"Repo cloned to {app_install_path}")

    # create seperate venv for that app
    venv_path = app_install_path / 'venv'
    subprocess.run(["python", "-m", "venv", str(venv_path)], check=True)
    logger.info("Virtual enviorment created")

    # get pip path based on OS
    if platform.system() == 'Windows':
      pip_path = venv_path / 'Scripts' / 'pip'
      logger.info("System identified as windows")
    else: # UNIX(mac/linux)
      pip_path = venv_path / 'bin' / 'pip'
      logger.info("System identified as UNIX (mac/linux)")
      
    # install requirements using specific venv's pip
    requirements = app_install_path / 'requirements.txt'
    if requirements.exists():
      subprocess.run([str(pip_path), "install", "-r", str(requirements)], check=True)
      logger.info("Dependancies installed successfully")
      
    # save to database
    add_installed_app(app_id, name, verison, repo_url)
    logger.info(f"Installation complete: {app_id}")

    return (True, "installation successful")
    
  except subprocess.CalledProcessError as e:
    return (False, f"Installation failed {e}")
  
def delete_app_files(app_id: str) -> Tuple[bool, str]:
  """Deletes app file(s) from disk"""
  try: 
    app_path = get_apps_dir() / app_id
    #Check if app cannot be found or succesfully already deleted
    if not app_path.exists():
      logger.warning(f"App folder not found: {app_path}")
      return (True, "Folder already deleted")
      
    #Removal function using shutil 
    shutil.rmtree(app_path)
    logger.info(f"Deleted app files: {app_path}")
    return(True, "File deletion successful")
    
  #Error log for unsuccessful deletion 
  except Exception as e:
    logger.error(f"Failed to delete app files: {e}")
    return(False, f"Deletction failed: {e}")
    
def uninstall_apps(app_id: str) -> Tuple[bool, str]:
    """Completely uninstall, removing files from disk & database"""
    try:
        deletion_successful, files_message = delete_app_files(app_id)

        if not deletion_successful:
            return (False, f"File deletion failed: {files_message}")

        remove_installed_apps(app_id)
        logger.info(f"Successfully uninstalled app: {app_id}")

        return (True, f"App '{app_id}' uninstalled successfully")

    # Error check file deletion unsuccessful
    except Exception as e:
        logger.error(f"Uninstall unsuccessful for {app_id}: {e}")
        return (False, f"Uninstall failed: {e}")

      

"""testing output"""
if __name__ == "__main__":
    # Test with a small repo
    success, message = install_app(
        app_id="test-app_manager",
        name="Test App",
        verison="1.0.0",
        repo_url="https://github.com/octocat/Hello-World"  # Small test repo
    )
    
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Check if it worked
    if success:
        print(f"\nCheck: {get_apps_dir() / 'test-app'}")

        #checking uninstall function
        input("\nPress Enter to test uninstall...")
        print("======Uninstalling Test Application======")
        success, message = uninstall_apps("test-app-mananger")
        print(f"Uninstall - Success: {success}")
        print(f"Uninstall - Message: {message}")
        
