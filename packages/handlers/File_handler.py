import os
from packages.loggers.base_logger import BaseLogger

import io
import json
import os
import logging
from ..loggers.base_logger import BaseLogger
from datetime import datetime

class FileHandler(BaseLogger):
    def __init__(self, logger: logging.Logger, storage_dir: str):
        self.logger = logger
        self.storage_dir = storage_dir
    
    def get_alpha(self, alpha_name):
        
        alpha_file = os.path.join(self.storage_dir, alpha_name, "code.txt")
        with open(alpha_file, "r") as f:
            alpha_code = f.read()
        return alpha_code.strip()
        
    
    