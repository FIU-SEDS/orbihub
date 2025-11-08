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