# orbihub

Modular marketplace platform for high-powered rocketry applications. Downloadable apps for telemetry, data analysis, firmware updates, and flight tools.

**Start small. Ship often. Stay focused.**

<div align="center">

[![python](https://img.shields.io/badge/Python-3.13-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

<a href="#Linux"><img src="https://img.shields.io/badge/os-linux-brightgreen">
<a href="#MacOS"><img src="https://img.shields.io/badge/os-mac-brightgreen">
<a href="#Windows"><img src="https://img.shields.io/badge/os-windows-red">

<a href="https://github.com/erielC"><img src="https://img.shields.io/badge/maintainer-erielC-blue"></a>
<a href="https://github.com/tomasmej"><img src="https://img.shields.io/badge/maintainer-tomasmej-blue"></a>
<a href = https://github.com/carlos-manuel-diaz><img src = https://img.shields.io/badge/maintainer-carlos_manuel_diaz-blue></a>

</div>

## 🎯 current focus (december 2025)

**immediate priority:** QThread implementation for non-blocking installation

### what works ✅
- PyQt6 desktop UI with aerospace theme
- SQLite database for tracking installed apps
- App cards display with images and styling  
- Uninstall functionality (Settings button)
- About dialog showing app information
- Logging system (file + console)
- Cross-platform path management
- App installation (blocks UI - being improved)

### in progress 🚧
- Install button functionality
- **Install button with QThread** - prevent UI freezing during git clone/venv creation
- App launching (detect installed apps, run with subprocess)
- Progress bar animation during installation
- **Uninstall button with QThread** - also prevents UI freezing

### planned 📋
- PyInstaller executable build
- User documentation
- Search/filter functionality (v1.1)
- Dynamic app registry from server (v2.0)

see [ROADMAP.md](ROADMAP.md) for long-term vision (phases 2-4)

## phase 1 progress (v1.0 - january 2026)

**completed:**
- [x] Phase 1: UI working (PyQt6 main window, app cards)
- [x] Phase 2: Data layer (SQLite database, app registry)
- [x] Phase 3: Display apps in UI (dynamic card generation)
- [x] Phase 4: Uninstall functionality with database cleanup
- [x] Phase 6 partial: theme styling, logging system

**current sprint (week of dec 13):**
- [ ] QThread for install_app() - prevent UI freeze
- [ ] Connect Install button to threaded worker
- [ ] Show animated progress bar during installation
- [ ] App launching capability

**next sprint (week of dec 20):**
- [ ] PyInstaller executable for macOS/Windows
- [ ] User documentation (README, usage guide)
- [ ] Beta testing with FIU SEDS team

**target:** December 22, 2026 - v1.0 release

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


## 📦 Installation

## Prerequisites
Before you begin, you will need to have Conda installed

### Installing Conda 
If you don't have Conda installed, download and install either:
- **[Anaconda](https://www.anaconda.com/products/distribution)** (Includes many pre-installed packages)
- **[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)** (Only includes Conda & Python)

** Verify Installation: **
```bash
conda --verison
```


### 1. Clone the Repository:
```bash
git clone https://github.com/FIU-SEDS/orbihub.git 
```

### 2. Create a Conda Enviornment:
Create a conda enviornment using the required dependencies: 
```bash
conda create -n orbihub python
```

### 3. Activate the Enviornment
```bash
conda activate orbihub
```

### 4. Install Dependencies

Install the required packages:
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python -m orbihub
```

## creating apps for orbihub

### required structure

All apps must follow this structure to work with OrbiHub:
```
your-app/
├── __main__.py          # Entry point (REQUIRED)
├── requirements.txt     # Dependencies (REQUIRED)
├── README.md            # Documentation (recommended)
└── your-app/            # Package folder (optional)
    └── ...
```

### requirements

**1. Entry Point (`__main__.py` at root)**
- Must be at the root level of your repository
- This file is executed when users click "Launch"
- Can import from subdirectories/packages

**Example `__main__.py`:**
```python
from your_app.main import run

if __name__ == "__main__":
    run()
```

**2. Dependencies (`requirements.txt`)**
- List all Python dependencies
- Will be installed in isolated virtual environment
- Standard pip format

**Example `requirements.txt`:**
```
PySide6>=6.6.0
numpy>=1.24.0
```

**3. Repository Structure**

OrbiHub will:
1. Clone your repository to `~/.orbihub/apps/{app-id}/`
2. Create a virtual environment
3. Install dependencies from `requirements.txt`
4. Run `__main__.py` when launching

### example app

See [pyside6-calculator](https://github.com/erielC/pyside6-calculator) for a complete example.

---
