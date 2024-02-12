# In src/textSummarizer/logging/logging.py

import os
import logging

def setup_logger(log_dir="logs", log_filename="running_logs.log"):
    """Set up logging configuration."""
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Define logging format
    logging_format = "[%(asctime)s] %(levelname)s: %(filename)s:%(lineno)d: %(message)s"

    # Set up logging to file
    log_filepath = os.path.join(log_dir, log_filename)
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(logging.Formatter(logging_format))

    # Set up logging to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(logging_format))

    # Get the root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return root_logger

# Call setup_logger() when this module is imported to configure logging
logger = setup_logger()
