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