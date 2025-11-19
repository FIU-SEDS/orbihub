from orbihub.utils.paths import get_database_file
from orbihub.utils.logger import logger
from typing import List
import sqlite3

def init_database():
  try:
    logger.info("Initilizing database...")
    db_path = get_database_file() # creates ~/.orbihub/ and returns db path
    conn = sqlite3.connect(db_path) # creates the .db file
    cursor = conn.cursor()
    
    # creating the tables
    """Note to self:
    SQLite functions:
    - Auto-incrementing unique ID (1, 2, 3, ...)
    - Primary key for the table
    - Unique cant have the same value twice
    - Not Null must have a value
    - Timestamp SQLite stores as ISO8601 string
    """
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS installed_apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_id TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        version TEXT NOT NULL,
        repo_url TEXT NOT NULL,
        installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
      )
    ''')
    conn.commit()
    conn.close()
    logger.info("Database created successfully")
  except Exception as e:
    logger.error(f"Database initlization error: {e}")
    raise # re-raising so caller is aware it failed
  
def get_installed_apps() -> List:
  """Get list of all installed apps from database"""
  try:
    db_path = get_database_file()
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM installed_apps")
      return cursor.fetchall()
  except Exception as e:
    logger.error(f"Error fetching installed apps: {e}")
    return []
    
def add_installed_app(app_id : str, name : str, version : str, repo_url : str):
  """Add a newly installed app to the database"""
  try:
    db_path = get_database_file()
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      cursor.execute("INSERT INTO installed_apps (app_id, name, version, repo_url) VALUES (?, ?, ?, ?)", 
                    (app_id, name, version, repo_url))
      conn.commit()
  except Exception as e:
    logger.error(f"Error adding app to database: {e}")
    raise # re-raising so install_app knows it failed


def remove_installed_apps(app_id : str):
  """Removes an app from the database"""
  try:
    db_path = get_database_file()
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      cursor.execute("DELETE FROM installed_apps WHERE app_id = ?", (app_id,))
      conn.commit()
      logger.info(f"Successfully removed app: {app_id}")
  except Exception as e:
    logger.error(f"Error removing application: {e}")
    raise


  
  
"""code for testing database"""
# if __name__ == "__main__":
#   print("Initalizing database...")
#   init_database()

#   print("\nAdding test app...")
#   add_installed_app("test-app-logging", "Test App", "1.0.0", "https://github.com/test/app")

#   print("\nInstalled Apps")
#   apps = get_installed_apps()
#   for app in apps:
#     print(app)