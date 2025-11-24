from PyQt6.QtCore import Qt
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

    self.setObjectName("appCard")

    # hidden by default until needed
    self.progress_bar.setVisible(False)
            
    # Style this specific widget
    self.setStyleSheet("""
        #appCard {
            background-color: #d5d5d5;
            border: 2px solid #BDC3C7;
            border-radius: 10px;
        }
        #appCard:hover {
            background-color: #E0E6E8;
            border: 2px solid #95A5A6;
        }
        QPushButton {
            background-color: #3498DB;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #2980B9;
        }
    """)

    # populate background color
    self.setAutoFillBackground(True)

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
