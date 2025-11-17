from PyQt6.QtWidgets import QMainWindow, QGridLayout
from orbihub.ui.ui_main_window import Ui_MainWindow
from orbihub.ui.apps_template.apps_frontend import form_apps
from pathlib import Path
from orbihub.utils.paths import get_project_root, get_home_dir

base_dir = get_project_root()
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect signals
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.searchButton.clicked.connect(self.search_apps)
    
                # appsGrid is already a QGridLayout, so you can directly add widgets to it
        orbiview_image_path = str(get_project_root() / 'assets' / 'orbiview_logo.png')
        app_1 = form_apps("Telemetry Viewer", orbiview_image_path, "1.0.0")
        self.ui.appsGrid.addWidget(app_1, 0, 0)
        
        app_2 = form_apps("Flight Data Analyzer", "assets/analyzer.png", "2.0.0")
        self.ui.appsGrid.addWidget(app_2, 0, 1)
        
        app_3 = form_apps("Sensor Calibration", "assets/sensor.png", "1.5.0")
        self.ui.appsGrid.addWidget(app_3, 1, 0)
        
        app_4 = form_apps("Ground Station", "assets/ground.png", "3.0.0")
        self.ui.appsGrid.addWidget(app_4, 1, 1)



    def search_apps(self):
        query = self.ui.searchLineEdit.text()
        print(f"Searching for: {query}")