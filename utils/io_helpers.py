# utils/io_helpers.py
import os
from config import constants

def ensure_output_dir():
    if not os.path.exists(constants.OUTPUT_DIR):
        os.makedirs(constants.OUTPUT_DIR)
