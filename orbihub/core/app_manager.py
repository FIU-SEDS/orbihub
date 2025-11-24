from orbihub.utils.paths import get_apps_dir
from orbihub.core.database import add_installed_app
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
    """Deletes app file(s) from marketplace utilizing shutil (shell utilities)"""
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
    
      
      #Error check file deletion unsuccessful 
    except Exception as e:
      logger.error(f"")

"""testing output"""
# if __name__ == "__main__":
#     # Test with a small repo
#     success, message = install_app(
#         app_id="test-app_manager",
#         name="Test App",
#         verison="1.0.0",
#         repo_url="https://github.com/octocat/Hello-World"  # Small test repo
#     )
    
#     print(f"Success: {success}")
#     print(f"Message: {message}")
    
#     # Check if it worked
#     if success:
#         print(f"\nCheck: {get_apps_dir() / 'test-app'}")