from PyQt6.QtWidgets import QMainWindow, QGridLayout
from orbihub.ui.ui_main_window import Ui_MainWindow
from orbihub.ui.styles import AEROSPACE_THEME
from orbihub.ui.apps_template.apps_frontend import form_apps
from pathlib import Path
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
     
        # appsGrid is already a QGridLayout, so you can directly add widgets to it
        # version and repo_url can become optional if needed
        app_1 = form_apps(
            "Telemetry Viewer",
            get_image_path('dashboard_logo.png'),
            "1.0.0",
            repo_url="https://github.com/org/telemetry-viewer.git",
            app_id="telemetry-viewer"
        )
        self.ui.appsGrid.addWidget(app_1, 0, 0)
        
        app_2 = form_apps(
            "Flight Data Analyzer",
            get_image_path('analyer_logo.png'),
            "2.0.0",
            repo_url="",
            app_id="flight-data-analyzer",
        )
        self.ui.appsGrid.addWidget(app_2, 0, 1)

        app_3 = form_apps(
            "Sensor Calibration",
            get_image_path('calculator_logo.png'),
            "1.5.0",
            repo_url="",
            app_id="sensor-calibration",
        )
        self.ui.appsGrid.addWidget(app_3, 1, 0)

        app_4 = form_apps(
            "Ground Station",
            "assets/ground.png",
            "3.0.0",
            repo_url="",
            app_id="ground-station",
        )
        self.ui.appsGrid.addWidget(app_4, 1, 1)



    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")
