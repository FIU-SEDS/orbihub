from orbihub.ui.apps_template.ui_app_template import Ui_app_template_format
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget
import sys

class MainWindow(QWidget, Ui_app_template_format):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()