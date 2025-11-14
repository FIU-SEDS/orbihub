#!/usr/bin/env python3
"""
Calculator Application Main Entry Point
"""
from PyQt6.QtWidgets import QApplication, QMainWindow
from orbihub.ui.main_window import MainWindow
import sys
# from .frontend import main  # Ensure 'frontend' is the correct module where 'main' is defined


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == '__main__':
    main()