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

        # Add image paths to each app
        apps[0]["image_path"] = get_image_path("dashboard_logo.png")
        apps[1]["image_path"] = get_image_path("analyer_logo.png")
        apps[2]["image_path"] = get_image_path("calculator_logo.png")
        apps[3]["image_path"] = get_image_path("ground.png")

        # appsGrid is already a QGridLayout, so you can directly add widgets to it
        app_1 = form_apps(apps[0])  # Pass whole dict
        self.ui.appsGrid.addWidget(app_1, 0, 0)

        app_2 = form_apps(apps[1])  # Pass whole dict
        self.ui.appsGrid.addWidget(app_2, 0, 1)

        app_3 = form_apps(apps[2])  # Pass whole dict
        self.ui.appsGrid.addWidget(app_3, 1, 0)

        app_4 = form_apps(apps[3])
        self.ui.appsGrid.addWidget(app_4, 1, 1)


    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")
