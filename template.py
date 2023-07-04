import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(ascitime)s]: %(messages)s:')


project_name = "textSummarizer"

list_of_files = [
".github/workflows/.gitkeep"
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/logging//__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/constants/__init__.py",
"config/config.yaml",
"params.yaml",
"app.py",
"main.py",
"dockerfile",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"test.py",

]


for fileplath in list_of_files:
    fileplath = Path(fileplath)
    filedir, filename = os.path.split(fileplath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")


    if (not os.path.exists(fileplath)) or (not os.path.getsize(fileplath)== 0):
        with open (fileplath, "w") as f:
            pass
            logging.info(f"Created empty file {filename}")
            



else:
   logging.info(f"{filename} already exists")

