#!/usr/bin/env python3
"""
Calculator Application Main Entry Point
"""
# from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from orbihub.ui.main_window import MainWindow
from orbihub.utils.logger import logger
from orbihub.utils.paths import get_image_path, get_project_root
from orbihub.core.database import init_database
import sys

# from .frontend import main  # Ensure 'frontend' is the correct module where 'main' is defined


def main():
    logger.info("Application starting up")
    app = QApplication(sys.argv)

    # Set application icon
    icon_path = str(get_project_root() / "assets" / "orbihub_icon.icns")
    # icon_path = str(get_image_path('orbihub_icon.icns'))
    app.setWindowIcon(QIcon(icon_path))  # ← Add this

    init_database()
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    logger.info("Application shutting down...")
    sys.exit(exit_code)  # using sys.exit() to preserve integrity of exit status


if __name__ == "__main__":
    main()
