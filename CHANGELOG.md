# Changelog

All notable changes to OrbiHub will be documented in this file.

## [0.1.3] - 2025-11-15

### Added
- App installation functionality with git clone automation
- Individual virtual environments (venv) per installed app
- Cross-platform pip path detection (Windows/Mac/Linux)
- Platform-agnostic installation checks (Git and Python verification)
- Automatic dependency installation from requirements.txt
- Integration between app_manager and database for tracking installations

### Changed
- Refactored checker utilities into separate module

### Fixed
- Path handling for cross-platform compatibility in app installation

## [0.1.2] - 2025-11-14

### Added
- core functionality for SQLite datbase (installing apps, details, etc)
- Introduced utility functions to get users home directory and ensuring `.orbihub` exists
- created app registry with a fetch_registry() to return list of available apps
- sys.exit(app.exec()) to return proper exit status

## [0.1.1] - 2025-11-13

### Added 
- Phase 1: Get Basic UI Working (DONE)
- .ui file to Python with pyuic6
- Created MainWindow class that loads the UI
- Updated main.py to launch the window
- Tested that window opens and buttons print messages when clicked

## [0.1.0] - 2025-11-08

### Added
- Project initialization

## [Unreleased]

### Added
- Initial project structure and file organization
- App registry system design
- Basic marketplace UI design
- PyQt6 integration with .ui to .py conversion workflow
- SQLite database schema for app management
- Configuration management for user data directories

### Fixed

---
