from PyQt6.QtWidgets import QMainWindow
from orbihub.ui.ui_main_window import Ui_MainWindow
from orbihub.ui.apps_template.apps_frontend import form_apps
from pathlib import Path
from orbihub.utils.paths import get_project_root

base_dir = get_project_root()
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect signals
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.searchButton.clicked.connect(self.search_apps)
    
        # live telemetry application 
        orbiview = form_apps()

    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")