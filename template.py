"""Module providing a function printing python version."""
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
]

# Create directories and files
for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Creating directory %s for the file %s", file_dir, file_name)

    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w", encoding="utf-8"):
            pass
        logging.info("Creating empty file: %s", file_path)
    else:
        logging.info("File %s already exists", file_name)
