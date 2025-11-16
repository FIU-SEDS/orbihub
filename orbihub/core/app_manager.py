from orbihub.utils.paths import get_apps_dir
from orbihub.core.database import add_installed_app
from orbihub.utils.checker import check_python_installed, check_git_installed 
from pathlib import Path
import os
import platform
import subprocess
from typing import Tuple

apps_dir = get_apps_dir()

def install_app(app_id : str, name : str, verison : str, repo_url : str) -> Tuple[bool, str]:
  if not (check_git_installed() and check_python_installed()):
    return (False, "Git or Python not installed")
      
  try:
    #git clone
    app_install_path = get_apps_dir() / app_id
    subprocess.run(["git", "clone", repo_url, str(app_install_path)], check=True)
    print(f"Repo cloned to {apps_dir}")

    # create seperate venv for that app
    venv_path = app_install_path / 'venv'
    subprocess.run(["python", "-m", "venv", str(venv_path)], check=True)

    # get pip path based on OS
    if platform.system() == 'Windows':
      pip_path = venv_path / 'Scripts' / 'pip'
    else: # UNIX(mac/linux)
      pip_path = venv_path / 'bin' / 'pip'
      
    # install requirements using specific venv's pip
    requirements = app_install_path / 'requirements.txt'
    if requirements.exists():
      subprocess.run([str(pip_path), "install", "-r", str(requirements)], check=True)
      
    # save to database
    add_installed_app(app_id, name, verison, repo_url)

    return (True, "installation successful")
    
  except subprocess.CalledProcessError as e:
    return (False, f"Installation failed {e}")

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