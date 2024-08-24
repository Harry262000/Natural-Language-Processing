# In main.py

import sys
import os

# Append the parent directory of main.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textSummarizer.logging.logging import logger

def main():
    logger.info("Welcome to our custom logging")

if __name__ == "__main__":
    main()

# Set the environment variable to disable symlink warnings
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'