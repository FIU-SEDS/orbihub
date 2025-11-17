#!/usr/bin/env python3
"""
Calculator Application Main Entry Point
"""
# from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication
from orbihub.ui.main_window import MainWindow
from orbihub.utils.logger import logger
import sys
# from .frontend import main  # Ensure 'frontend' is the correct module where 'main' is defined


def main():
    logger.info("Application starting up")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    logger.info("Application shutting down...")
    sys.exit(exit_code) # using sys.exit() to preserve integrity of exit status
if __name__ == '__main__':
    main()