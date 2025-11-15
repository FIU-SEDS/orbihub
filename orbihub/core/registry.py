from typing import List

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
   "id": "rocket-calculator",
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
  }
]

# function to return apps
def fetch_registry() -> List:
  # return the list of apps
  return sample_apps
  
# testing the code
if __name__ == "__main__":
  apps_list = fetch_registry()
  for app in apps_list:
    print(f"{app['name']}- v{app['version']}\n\t{app['description']}\n")