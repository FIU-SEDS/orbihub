from PyQt6.QtWidgets import QMainWindow, QGridLayout
from orbihub.ui.ui_main_window import Ui_MainWindow
from orbihub.ui.styles import AEROSPACE_THEME
from orbihub.ui.apps_template.apps_frontend import form_apps
from pathlib import Path
from orbihub.core.registry import fetch_registry
from orbihub.utils.paths import get_project_root, get_home_dir, get_image_path

base_dir = get_project_root()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet(AEROSPACE_THEME)

        # Connect signals
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.searchButton.clicked.connect(self.search_apps)

        apps = fetch_registry()

        # automatically add app into interface
        for index, app in enumerate(apps):
            app["image_path"] = get_image_path(app["image"])
            card = form_apps(app)
            row = index // 2
            col = index & 2
            self.ui.appsGrid.addWidget(card, row, col)
            
    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")
