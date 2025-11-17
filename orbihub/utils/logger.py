from orbihub.utils.paths import get_logs_dir
import logging

def setup_logger():
  """reason we are using both types of handlers file/stream is so one is printed to ~/.orbihub/logs/orbihub.log and the other is printed to the console"""

  log_path = get_logs_dir() / 'orbihub.log'
  logger = logging.getLogger("orbihub")
  logger.setLevel(logging.INFO)  

  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

  file_handler = logging.FileHandler(log_path)
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)

  console_handler = logging.StreamHandler() # prints to the console
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)

  return logger

logger = setup_logger()