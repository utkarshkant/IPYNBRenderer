import os
from pathlib import Path    # makes application OS independent
import logging              # helps log and track progress and helps with debugging

# set basic configuration for logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(ascitime)s: %(levelname)s]: %(message)s",    # log record format
)

# fetch project name from user
while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":      # keep the loop running until the project name is entered
        break

logging.info(f"Creating Project by Name: {project_name}")

# create list of the files
list_of_files = [
    ".github/workflows/.gitkeep",       # empty file to keep the structure intact
    f"src/{project_name}/__init__.py",  # source repository that will keep all the files
    f"tests/__init__.py",               # test repository 
    f"tests/unit/__init__.py",          # test repository 
    f"tests/integration/__init__.py",   # test repository 
    "init_setup.sh",                    # environment setup
    "requirements.txt",                 # package requirements
    "requirements_dev.txt",             # for package testing
    "setup.py",                         # basic setup file
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",                          # helps test package with different python environments    

]

# create files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    
    # if directory is empty then create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for {filename}")
    
    # if file does not exist then create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"File is already present at: {filepath}")

