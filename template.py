from pathlib import Path
import logging
from typing import List, Set


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(lineno)s:%(name)s:%(message)s',
    handlers= [
        logging.FileHandler('templates.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

project_name = "cnnClassifier"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
]


def create_files_and_directories(list_of_files: List[str]) -> None:
    '''Create directories and files from the list of filespath.'''
    created_directories : Set[Path] = set()
    for file in list_of_files:
        try:
            path = Path(file)
            if not path.exists():
                if path.parent not in created_directories:
                    logger.info(f'creating parent directory {path.parent} for {file}')
                    path.parent.mkdir(parents=True, exist_ok=True)
                    created_directories.add(path.parent)
                if not path.suffix and path not in created_directories: # if it's a directory
                    logger.info(f'creating directory for {file}')
                    path.mkdir(parents=True, exist_ok=True)
                    created_directories.add(path)
                else: # if it's a file
                    logger.info(f'creating file for {file}')
                    path.touch()
            else:
                logger.info(f'file {file} already exists.')
        except Exception as e:
            logger.error(f'Error processing {file}:{e}')

create_files_and_directories(list_of_files)
