"""
QThread Learning Test
Practice QThread basics before implementing in real app
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import time


class TestWorker(QThread):
  """Simple worker to understand QThread"""

  # Define signals (messages this worker can send)
  progress = pyqtSignal(int)  # Send percentage 0-100
  finished = pyqtSignal(str)  # Send final message

  def run(self):
    """This method runs in the background thread"""
    print("Worker started!")

    # Simulate slow work with progress updates
    for i in range(11):  # 0 to 10
      time.sleep(0.5)  # Pretend we're doing slow work
      percentage = i * 10
      print(f"Worker: {percentage}% done")
      self.progress.emit(percentage)  # Send progress signal

    print("Worker finished!")
    self.finished.emit("All done!")  # Send finished signal


class TestWindow(QMainWindow):
  """Simple window to test the worker"""

  def __init__(self):
    super().__init__()
    self.setWindowTitle("QThread Test")
    self.setGeometry(100, 100, 400, 200)

    # Create UI
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    layout = QVBoxLayout(central_widget)

    # Label to show progress
    self.label = QLabel("Click button to start worker")
    layout.addWidget(self.label)

    # Button to start worker
    self.button = QPushButton("Start Worker")
    self.button.clicked.connect(self.start_worker)
    layout.addWidget(self.button)

    # Store worker reference
    self.worker = None

  def start_worker(self):
    """Start the background worker"""
    print("Starting worker...")
    self.button.setEnabled(False)
    self.label.setText("Working...")

    # Create worker
    self.worker = TestWorker()

    # Connect signals to slots (methods)
    self.worker.progress.connect(self.on_progress)
    self.worker.finished.connect(self.on_finished)

    # Start the worker thread
    self.worker.start()

  def on_progress(self, percentage):
    """Called when worker sends progress update"""
    print(f"UI received: {percentage}%")
    self.label.setText(f"Progress: {percentage}%")

  def on_finished(self, message):
    """Called when worker finishes"""
    print(f"UI received: {message}")
    self.label.setText(f"Finished! {message}")
    self.button.setEnabled(True)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = TestWindow()
  window.show()
  sys.exit(app.exec())