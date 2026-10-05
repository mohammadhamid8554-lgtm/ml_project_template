import logging
import os
from datetime import datetime

# --- 🔗 CONNECTIONS ---
# This file doesn't import from our project. Instead, it is IMPORTED BY almost 
# every other file in the project (like main.py and app.py) to record what happens.

# 1. Create a "logs" folder in the current working directory if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 2. Name the log file based on the exact current date and time (e.g., 09_18_2026_16_30_00.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# 3. Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    # This format records: [Timestamp] Line_Number File_Name - Message
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # INFO means it records general updates, warnings, and errors
    force=True,
)
