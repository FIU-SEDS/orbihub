#!/usr/bin/env python3
"""
Calculator Application Main Entry Point
"""
from PyQt6.QtWidgets import QApplication, QMainWindow
from orbihub.ui.ui_main_window import Ui_MainWindow
import sys
# from .frontend import main  # Ensure 'frontend' is the correct module where 'main' is defined

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect signals
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.searchButton.clicked.connect(self.search_apps)
    
    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")

if __name__ == '__main__':
    # main()  # Call the main function to start the application
# from PyQt6.QtWidgets import QMainWindow ,QWidget
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()