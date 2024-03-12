from pathlib import Path
from typing import Any
import json
from box.exceptions import BoxValueError
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from cnnClassifier import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose:bool=True):
    """
    create list of directories

    Args:
    path_to_directories: list of file paths
    verbose (bool, optional): Turn on/off logs, default to True

    Returns:
    None
    """
    created_directory = set()
    for dir_path in path_to_directories:
        if dir_path not in created_directory:
            created_directory.add(dir_path)
            try:
                dir_path = Path(dir_path)
                assert not dir_path.suffix, f'{str(dir_path)} is not a directory'
                dir_path.mkdir(parents=True, exist_ok=True)
                if verbose:
                    logger.info(f'Created directory for {str(dir_path)}')
            except Exception as e:
                logger.error(f'Error processing for {dir_path} : {e}')
        else:
            logger.info(f'Directory path:{str(dir_path)} already exists')

@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data

    Parameters
    ----------
    path : Path
        path to save json file.
    data : dict
        data to be saved in json.

    Returns
    -------
    None.

    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f'json file saved at: {path}')

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """
    load json files data

    Parameters
    ----------
    path : Path
        path of json file.

    Returns
    -------
    ConfigBox
        json file data in configbox format.

    """
    with open(path, 'r') as f:
        content = json.load(f)
    
    logger.info(f'json file loaded successfully from:{path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    Parameters
    ----------
    data : Any
        data to be saved as binary.
    path : Path
        path to binary file.

    Returns
    -------
    None.

    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    Parameters
    ----------
    path : Path
        path to binary file.

    Returns
    -------
    Any
        object stored in the file.

    """
    data = joblib.load(path)
    logger.info(f'loaded binary data from path:{path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in kb

    Parameters
    ----------
    path : Path
        path of the file.

    Returns
    -------
    str
        size in kb.

    """
    assert path.exists(), f'No such file:{path}'
    size_in_kb = round(path.stat().st_size/1024)
    logger.info('The size of {path} is ~ {size_in_kb}')
    return f"~ {size_in_kb} KB"

        
