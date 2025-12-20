from typing import List
from orbihub.utils.logger import logger

sample_apps =[
  {
    "id": "telemetry-viewer",
    "name": "Live Telemetry Viewer",
    "description": "Real-time rocket telemetry monitoring",
    "version": "1.0.0",
    "repo": "https://github.com/fiu-seds/telemetry-viewer",
    "author": "FIU SEDS"
  },
  {
   "id": "rocketcalc",
    "name": "Rocket Calculator",
    "description": "Calculator to calculate snatch force, ejection force, etc",
    "version": "1.0.0",
    "repo": "https://github.com/fiu-seds/rocket-calculator",

    "author": "FIU SEDS"
  },
  {
    "id": "flight-data-analyzer",
    "name": "Post Flight Data Analyzer",
    "description": "Can review and playback past flight data",
    "version": "1.0.0",
    "repo": "https://github.com/fiu-seds/flight-data-analyzer",
    "author": "FIU SEDS"
  },
  {
    "id": "calculator",  # ← Add this one
    "name": "PySide6 Calculator",
    "description": "Simple calculator app for testing OrbiHub installation",
    "version": "1.0.0",
    "repo": "https://github.com/erielC/pyside6-calculator",
    "author": "Test",
    "image": "calculator_logo.png"  # Reuse calculator image
  }
]

# function to return apps
def fetch_registry() -> List:
  # return the list of apps
  logger.info("Fetching apps in registry")
  return sample_apps
  
# # testing the code
# if __name__ == "__main__":
#   apps_list = fetch_registry()
#   for app in apps_list:
#     print(f"{app['name']}- v{app['version']}\n\t{app['description']}\n")