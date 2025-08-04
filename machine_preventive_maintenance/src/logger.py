import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Optional: Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console)

if __name__ == "__main__":
    logging.info("Logging has started successfully.")
