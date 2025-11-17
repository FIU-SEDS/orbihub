"""
Path utilities for OrbiHub.
Provides platform-independent paths for data, apps, and project files.
"""
from pathlib import Path
import os
import sys

def get_project_root() -> Path:
  """Get the Orbihub project root directory

  Returns:
      Path: absolute path to orbihub/ directory
      
  Example:
      /Users/username/projects/orbihub
  """
  # all utils files are in orbihub/utils/path.py
  # so parent.parent gets this to orbihub/
  return Path(__file__).parent.parent

def get_base_dir() -> Path:
  """
  Get the base directory where orbihub is installed.
  Same as the get_project_root() but more explicit name.
  """
  return get_project_root()

def get_home_dir() -> Path:
  """Get the home directory of the users computer
  
  Returns:
    Path: home directory path
    
  Example:
    /Users/username/ or ~
  """
  return Path.home()

def get_ui_file(filename : str) -> Path:
  """Goes to the ui directory from base
  
  Returns:
    Path: absolute path to the ui/ directory
    
  Example:
    /Users/username/projects/orbihub/orbihub/ui
  """
  return get_project_root / 'ui' / filename

def get_apps_dir() -> Path:
  apps_dir = get_home_dir() / '.orbihub'
  apps_dir.mkdir(parents=True, exist_ok=True)
  return apps_dir

def get_data_dir() -> Path:
  data_dir = get_home_dir() / '.orbihub'
  data_dir.mkdir(parents=True, exist_ok=True)
  return data_dir

def get_database_file() -> Path:
  """Get path to SQLite database file

  Returns:
      Path: Database file path (~/.orbihub/orbihub.db)
  """
  return get_data_dir() / 'orbihub.db'

def get_logs_dir() -> Path:
  """Gets the path to the logger directory for application debugging
  
  Returns:
    Path: logger directory
  """ 
  logs_dir = get_home_dir() / '.orbihub'
  # creates the directory if it doesnt exists
  logs_dir.mkdir(parents=True, exist_ok=True)
  return logs_dir