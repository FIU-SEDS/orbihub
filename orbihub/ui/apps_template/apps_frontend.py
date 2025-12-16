from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from orbihub.ui.apps_template.ui_app_template import Ui_app_template_format
from orbihub.utils.logger import logger
from orbihub.core.app_manager import uninstall_apps, install_app


class form_apps(QWidget, Ui_app_template_format):
    """
    The template Ui to create homepage apps.

    Class sets up the Ui for the home page and initializes the components defined in the Ui file
    """
    def __init__(self, app_name: str, image_path: str, version: str, repo_url: str, app_id: str):
        """sets up the ui file to display in the application"""
        super().__init__()
        self.setupUi(self)

        # store properties
        self.app_name = app_name
        self.app_id = app_id
        self.version = version
        self.repo_url = repo_url

        self.setObjectName("appCard")

        # hidden by default until needed
        self.progress_bar.setVisible(False)

        # Force Qt to draw the styled background
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
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
                background-color: white;
                border: none;
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
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load image
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
            logger.info(f"Image loaded: {image_path}")
        else:
            self.image_label.setText("No Image")
            logger.error(f"Failed to load image: {image_path}")

        # Add label to layout
        image_layout.addWidget(self.image_label)

        # wire up install button
        self.install_button.clicked.connect(self.on_installed_clicked)

    def on_installed_clicked(self):
        """Handles install button click"""
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
                self.install_button.setText("Installed")

                # Optionally set progress bar to 100 here

            else:
                logger.error(f"Installation failed: {message}")
                self.install_button.setEnabled(True)
                self.install_button.setText("Install")

        except Exception as e:
            logger.error(f"Error during install of {self.app_name}: {e}")
            self.install_button.setEnabled(True)
            self.install_button.setText("Install")
