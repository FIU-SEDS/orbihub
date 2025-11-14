from PyQt6.QtWidgets import QWidget
from orbihub.ui.apps_template.ui_app_template import Ui_app_template_format

class form_apps(QWidget, Ui_app_template_format):
  """
  The template Ui to create homepage apps.
  
  Class sets up the Ui for the home page and initializes the components defined in the Ui file
  """
  def __init__(self):
    """sets up the ui file to display in the application"""
    super().__init__()

    self.setupUi(self)