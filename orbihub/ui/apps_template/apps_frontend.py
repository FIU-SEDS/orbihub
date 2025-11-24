from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from orbihub.ui.apps_template.ui_app_template import Ui_app_template_format
from orbihub.utils.logger import logger

class form_apps(QWidget, Ui_app_template_format):
  """
  The template Ui to create homepage apps.
  
  Class sets up the Ui for the home page and initializes the components defined in the Ui file
  """
  def __init__(self, app_name : str, image_path : str, version : str):
    """sets up the ui file to display in the application"""
    super().__init__()
    self.setupUi(self)

    # styling the app card and buttons alike
    self.setStyleSheet("""
    QFrame {
        background-color: #ECF0F1;
        border: 1px solid #BDC3C7;
        border-radius: 10px;
        padding: 15px;
    }
    QFrame:hover {
        background-color: #E0E6E8;
        border: 1px solid #95A5A6;
    }
    """)
    
    self.install_button.setStyleSheet("""
    QPushButton {
        background-color: #3498DB;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
    QPushButton:pressed {
        background-color: #21618C;
    }
    """)

    self.settings_button.setStyleSheet("""
    QPushButton {
        background-color: #3498DB;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
    QPushButton:pressed {
        background-color: #21618C;
    }
    """)

    self.about_button_3.setStyleSheet("""
    QPushButton {
        background-color: #3498DB;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
    QPushButton:pressed {
        background-color: #21618C;
    }
    """)


    image_label = QLabel(parent=self.app_image)
    image_label.setScaledContents(True)
    image_label.setGeometry(self.app_image.rect())
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        logger.error(f"Failed to load image: {image_path}")
    else:
        logger.info(f"Image loaded successfully: {pixmap.size()}")
    image_label.setPixmap(pixmap) 


