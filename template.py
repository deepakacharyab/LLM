import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

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

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory %s for the file %s", filedir, filename)

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w", encoding="utf-8"):
            pass
        logging.info("Creating empty file: %s", filepath)
    else:
        logging.info("%s already exists", filename)
