"""Test path utilities"""
from orbihub.utils.paths import get_data_dir, get_apps_dir, get_home_dir
from pathlib import Path

def test_get_data_dir():
  """Test that data directory is created"""
  data_dir = get_data_dir()
  
  # Check it's a Path object
  assert isinstance(data_dir, Path)
  
  # Check it exists
  assert data_dir.exists()
  
  # Check it ends with .orbihub
  assert data_dir.name == '.orbihub'

def test_get_apps_dir():
  """Test that apps directory is created"""
  apps_dir = get_apps_dir()
  
  assert isinstance(apps_dir, Path)
  assert apps_dir.exists()
  assert apps_dir.name == 'apps'

def test_get_home_dir():
  """Test taht home path is created"""
  home = get_home_dir()

  # check it's a path object
  assert isinstance(home, Path)

  # should exists
  assert home.exists()

  # should be a directory, not a file
  assert home.is_dir()

  # matches python's Path.home()
  assert home == Path.home()
