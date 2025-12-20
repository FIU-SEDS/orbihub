from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QPixmap
from orbihub.ui.apps_template.ui_app_template import Ui_app_template_format
from orbihub.utils.logger import logger
from orbihub.core.app_manager import uninstall_app, install_app, app_launch
from orbihub.core.registry import fetch_registry

class form_apps(QWidget, Ui_app_template_format):
    """
    The template Ui to create homepage apps.

    Class sets up the Ui for the home page and initializes the components defined in the Ui file
    """
    def __init__(self, app_data: dict):
        """sets up the ui file to display in the application"""
        super().__init__()
        self.setupUi(self)
        
        # link functions to buttons
        self.install_button.clicked.connect(lambda: self.handle_install())
        self.about_button_3.clicked.connect(lambda: self.handle_about())
        self.settings_button.clicked.connect(lambda: self.handle_settings())

        # Extract all data from dict
        self.app_data = app_data
        self.app_id = app_data["id"]
        self.app_name = app_data["name"]
        self.version = app_data["version"]
        self.repo_url = app_data["repo"]
        self.description = app_data["description"]
        self.author = app_data["author"]
        image_path = app_data["image_path"]

        self.setObjectName("appCard")

        # hidden by default until needed
        self.progress_bar.setVisible(False)

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground, True
        )  # rendering background color for entire widget not just child elements

        self.setStyleSheet(
        """
        QWidget#appCard {
            background-color: white;
            border: 2px solid #0B3D91;
            border-radius: 12px;
            padding: 15px;
        }
        QWidget#appCard:hover {
            background-color: #F0F4F8;
            border: 3px solid #E8B923;
        }
        QPushButton {
            background-color: #0B3D91;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px;
            font-weight: bold;
            font-size: 12px;
        }
        QPushButton:hover {
            background-color: #E8B923;
            color: #1C2541;
        }
        QPushButton:pressed {
            background-color: #1C2541;
            color: white;
        }
        QFrame#app_image {
            background-color: white;        /* ← same as card, no separate color */
            border: none;                         /* ← No border on image frame */
            border-radius: 8px;
        }
        """)

        # Set image frame size
        self.app_image.setFixedSize(220, 220)

        # Create layout for app_image frame
        image_layout = QVBoxLayout(self.app_image)
        image_layout.setContentsMargins(0, 0, 0, 0)

        # Create label
        self.image_label = QLabel()
        self.image_label.setScaledContents(True)  # Auto-scale
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load image
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)  # Qt handles scaling
            logger.info(f"Image loaded: {image_path}")
        else:
            self.image_label.setText("No Image")
            logger.error(f"Failed to load image: {image_path}")

        # Add label to layout
        image_layout.addWidget(self.image_label)

        app_list = fetch_registry()

    def handle_launch(self):
        """Launch installed app"""
        logger.info(f"Launching {self.app_name}...")

        success, message = app_launch(self.app_id)

        if success:
            logger.info(f"Successfully launched {self.app_name}")
        else:
            QMessageBox.information(
                self,
                "Launch App",
                f"Launching {self.app_name}...\n(Not implemented yet)"
            )



    def handle_install(self):
        """Handles install OR launch button click"""
        # Check what the button currently says
        button_text = self.install_button.text()

        if button_text == "Launch":
            # App is already installed - launch it
            self.handle_launch()
        else:
            logger.info(f"Attempting to install: {self.app_name}")

            # Prevent user from double clicking 'install' button
            self.install_button.setEnabled(False)
            self.install_button.setText("Installing...")

            try:
                success, message = install_app(
                    app_id=self.app_id,
                    name=self.app_name,
                    version=self.version,
                    repo_url=self.repo_url,
                )
                if success:
                    logger.info(f"Installation successful: {self.app_name}")
                    self.install_button.setText("Launch")
                    self.install_button.setEnabled(True)
                    self.settings_button.setEnabled(True)
                    # Optionally set progress bar to 100 here

                else:
                    logger.error(f"Installation failed: {message}")
                    self.install_button.setEnabled(True)
                    self.install_button.setText("Install")

            except Exception as e:
                logger.error(f"Error during install of {self.app_name}: {e}")
                self.install_button.setEnabled(True)
                self.install_button.setText("Install")


    def handle_about(self):
        message = f"{self.app_name}\n"
        message = f"{self.app_name}\n"
        message += f"Version: {self.version}\n"
        message += f"Author: {self.author}\n\n"
        message += f"App Description: {self.description}\n\n"
        message += f"Repository: {self.repo_url}"

        QMessageBox.information(self, f"About {self.app_name}", message)

        
    def handle_settings(self):
        # uninstall directly
        success, message = uninstall_app(self.app_id)

        # show result
        if success:
            self.settings_button.setEnabled(False)
            self.install_button.setText("Install")
            self.install_button.setEnabled(True)

            logger.info(f"Successfully deleted {self.app_id}")
        else:
            # show error
            QMessageBox.critical(
                self,
                "Uninstall failed",
                f"Failed to uninstall {self.app_name}: {message}",
            )