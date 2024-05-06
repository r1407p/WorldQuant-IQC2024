import os
from configs.log_config import LogConfig
from packages.loggers.base_logger import BaseLogger
from packages.handlers.Setting_handler import Setting
from packages.handlers.File_handler import FileHandler
from packages.handlers.Client_handler import ClientHandler

import requests

class WorldQuantEngine(BaseLogger):
    def __init__(self, email: str, password: str, log_config: LogConfig, alpha_name):
        super().__init__(log_config)
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.alpha_name = alpha_name
        self.file_handler = FileHandler(self.logger, "alphas")
        self.client_handler = ClientHandler(self.logger, self.session)
        self.login()
        
    def login(self):
        try:
            res = self.session.post('https://api.worldquantbrain.com/authentication', auth=(self.email, self.password))
            res.raise_for_status()
            self.logger.info('Logged in successfully')
            
        except Exception as e:
            self.logger.error(f'Failed to login: {e}')
            return
        
    def simulate(self):
        all_settings = Setting.get_settings()
        alpha_code = self.file_handler.get_alpha(self.alpha_name)
        links = []
        for i in range(len(all_settings)):
            links.append(self.client_handler.send_alpha(all_settings[i], alpha_code))
            self.logger.info(f'Simulation {i+1} started successfully')            
        
        