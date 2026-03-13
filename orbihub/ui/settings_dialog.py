from PyQt6.QtWidgets import QDialog, QMessageBox
from orbihub.ui.ui_settings_dialog import Ui_Dialog
from orbihub.ui.styles import AEROSPACE_THEME
# from orbihub.ui.apps_template.apps_frontend import form_apps
from pathlib import Path
from orbihub.utils.logger import logger
from orbihub.core.registry import fetch_registry
from orbihub.utils.paths import get_project_root, get_home_dir, get_image_path
from orbihub.core.app_manager import uninstall_app

class SettingsDialog(QDialog):
    def __init__(self, app_id, app_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setStyleSheet(AEROSPACE_THEME)
        self.ui.deleteButton.setProperty("dialogIcon", "large")
        self.ui.configButton.setProperty("dialogIcon", "large")

        # Connect signals
        self.ui.deleteButton.clicked.connect(lambda: self.handle_delete(app_id, app_name))
        self.ui.deleteButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)

    def handle_delete(self, app_id, app_name):

        try:
            self.uninstall_results = uninstall_app(app_id)
        except Exception as e:
            # show error
            QMessageBox.critical(
                self,
                "Uninstall failed",
                f"Failed to uninstall {self.app_name}: {self.uninstall_results[1]}",
            )

    
    def get_uninstall_results(self):
        return self.uninstall_results

        # show result
        # if success:
        #     self.settings_button.setEnabled(False)
        #     self.install_button.setText("Install")
        #     self.install_button.setEnabled(True)

        #     logger.info(f"Successfully deleted {app_id}")
        # else:
        #     # show error
        #     QMessageBox.critical(
        #         self,
        #         "Uninstall failed",
        #         f"Failed to uninstall {app_name}: {message}",
        #     )