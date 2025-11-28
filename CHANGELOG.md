# Changelog

All notable changes to OrbiHub will be documented in this file.

## [0.1.6] - 2025-11-27

### Added
- Aerospace-themed UI design with NASA-inspired color palette
- Custom app icon support for macOS and Windows
- PyInstaller build configuration for standalone app distribution
- Dynamic app card styling with hover effects
- White card backgrounds with navy blue borders and gold accents
- Application icon in window title bar and dock

### Changed
- Updated UI color scheme to aerospace theme (navy #0B3D91, gold #E8B923)
- Improved app card layout with proper background rendering
- Set app images to square format (220x220px) for consistent display
- Enhanced button styling with aerospace color palette
- Updated main window with dark title bar and professional spacing

### Fixed
- App card background now renders correctly with WA_StyledBackground attribute
- Removed unsupported CSS properties (box-shadow) from stylesheets
- Fixed image aspect ratio distortion in app cards
- Corrected stylesheet syntax errors (removed Python comments from CSS)
- Fixed asset path issues for consistent image loading

### Technical
- Created `orbihub/ui/styles.py` for centralized theme management
- Preparing PyInstaller configuration for app bundling
- Added support for .icns icon format on macOS


## [0.1.5] - 2025-11-24

### Added
- App card UI component with rounded borders and hover effects
- Image display functionality for app logos in cards
- Fixed-size app cards (400x350px) with proper image scaling
- Square image frame (220x220px) for 1:1 aspect ratio logos
- Styled buttons (About, Install, Settings) with hover states
- Progress bar component (hidden by default until installation)

### Changed
- Improved app card styling with background colors and borders
- Set app cards to fixed size to prevent stretching in grid layout
- Image scaling now maintains aspect ratio without distortion

### Fixed
- App card background now properly renders with styled background attribute
- Images now display at correct proportions (1:1 ratio for square logos)
- Path handling for app images now uses full paths consistently

## [0.1.4] - 2025-11-16

### Added
- Comprehensive logging system with file and console output
- Logs stored in `~/.orbihub/logs/orbihub.log`
- Logging for app installation events and errors
- Logging for database operations
- Logging for app registry fetching
- Application startup and initialization logging

### Changed
- Replaced print statements with structured logging throughout codebase
- Improved error handling with detailed error logs

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
