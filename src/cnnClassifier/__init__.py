import os
import sys
import logging
from pathlib import Path


logging_str = '%(asctime)s:%(levelname)s:%(lineno)s:%(module)s:%(name)s:%(message)s'
log_dir = 'logs'
log_filepath = Path(log_dir, 'running_logs.log')
log_filepath.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)