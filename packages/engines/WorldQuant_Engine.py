from configs.log_config import LogConfig
from packages.loggers.base_logger import BaseLogger

import requests

class WorldQuantEngine(BaseLogger):
    def __init__(self, email: str, password: str, log_config: LogConfig):
        super().__init__(log_config)
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.login()
        
    def login(self):
        try:
            res = self.session.post('https://api.worldquantbrain.com/authentication', auth=(self.email, self.password))
            res.raise_for_status()
            self.logger.info('Logged in successfully')
            
        except Exception as e:
            self.logger.error(f'Failed to login: {e}')
            return
        
        