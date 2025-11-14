# orbihub
Modular marketplace platform for high-powered rocketry applications. Downloadable apps for telemetry, data analysis, firmware updates, and flight tools.


## plan

```bash
orbihub-project/
├── orbihub/                    # Your source code package
│   ├── __init__.py
│   ├── __main__.py
│   ├── ui/
│   ├── core/
│   └── utils/
│
├── assets/                     # Static resources (shipped with code)
│   ├── icons/
│   └── default_config.json
│
├── docs/
├── licenses/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

# User's machine (created at runtime, NOT in repo):
~/.orbihub/                     # or ~/orbihub-data/
├── apps/                       # Downloaded marketplace apps
│   ├── telemetry-viewer/
│   ├── data-replay/
│   └── flight-analyzer/
├── data/                       # User's CSV files, logs
│   ├── flight_001.csv
│   ├── flight_002.csv
│   └── telemetry_logs/
└── config.json                 # User settings
```

- For ui/ folder:
PyQt6 user interface components including main marketplace window, app cards, and dialogs. Contains both .ui designer files and generated Python UI code.

- For core/ folder:
Core business logic for app management including installation via git, registry fetching, database operations, and app launching.

- For utils/ folder:
Utility functions and helpers for configuration management, logging, validation, and app-wide constants.

```bash
Development Steps (In Order)
Phase 1: Get Basic UI Working (DONE)
Step 1: Convert your .ui file to Python with pyuic6
Step 2: Create MainWindow class that loads the UI
Step 3: Update main.py to launch the window
Step 4: Test that window opens and buttons print messages when clicked

Phase 2: Set Up Data Layer
Step 5: Create database.py with SQLite tables for installed apps
Step 6: Test database creation by running the file directly
Step 7: Create registry.py with hardcoded sample apps list
Step 8: Test registry by printing sample appsx-

Phase 3: Display Apps in UI
Step 9: Create AppCard widget class (displays one app)
Step 10: Update MainWindow to fetch apps from registry
Step 11: Add app cards to the grid layout dynamically
Step 12: Test that app cards appear in the window

Phase 4: Implement Installation
Step 13: Create app_manager.py with git clone function
Step 14: Connect "Install" button on cards to app_manager
Step 15: Test installing an app (git clone to ~/.orbihub/apps/)
Step 16: Save installation record to database
Step 17: Show success/error messages to user

Phase 5: Add More Features
Step 18: Implement uninstall functionality (delete folder + database record)
Step 19: Add search/filter for apps
Step 20: Add app launching capability
Step 21: Add update checking for installed apps

Phase 6: Polish & Distribute
Step 22: Add styling/themes to make it look professional
Step 23: Add error handling and logging
Step 24: Create executable with PyInstaller
Step 25: Test on clean machine
Step 26: Write user documentation
Step 27: Release to your club!

Your Current Position
DONE UI designed
DONE paths.py written
Next: Start Phase 1, Step 1 (convert .ui to Python)
Suggested Work Sessions

Session 1: Steps 1-4 (Get window opening)
Session 2: Steps 5-8 (Database + registry)
Session 3: Steps 9-12 (Show apps in UI)
Session 4: Steps 13-17 (Install apps)
Session 5+: Steps 18-27 (Features + polish)

Focus on completing Phase 1 first. Don't jump ahead!
Which phase/step are you starting with?
```
