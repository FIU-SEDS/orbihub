#!/usr/bin/env python3
"""
Calculator Application Main Entry Point
"""
# from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication
from orbihub.ui.main_window import MainWindow
import sys
# from .frontend import main  # Ensure 'frontend' is the correct module where 'main' is defined


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) # using sys.exit() to preserve integrity of exit status

if __name__ == '__main__':
    main()