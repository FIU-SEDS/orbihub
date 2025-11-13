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
      /Users/eriel/projects/orbihub
  """
  # all utils files are in orbihub/utils/path.py
  # so parent.parent gets this to orbihub/
  return Path(__file__).parent.parent

def get_base_dir() -> Path:
  """
  Get the base directory where orbihub is installed.
  Same as the get_project_root() but more explicit name.
  """