import logging
import os

LOG_DIR = "app/logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)

logger = logging.getLogger(
    "ecommerce_backend"
)

logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# Avoid adding handlers multiple times
if not logger.handlers:

    file_handler = logging.FileHandler(LOG_FILE)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)