import os
from packages.loggers.base_logger import BaseLogger

import json
import time
import requests
import os
import logging
from ..loggers.base_logger import BaseLogger
from datetime import datetime

class ClientHandler(BaseLogger):
    def __init__(self, logger: logging.Logger, session: requests.Session):
        self.logger = logger
        self.session = session
    def send_alpha(self, alpha_settings: dict, alpha_code: str):
        while True:
            try:
                res = self.session.post('https://api.worldquantbrain.com/simulations', json={
                    'regular': alpha_code,
                    'type': 'REGULAR',
                    'settings': alpha_settings
                })
                res.raise_for_status()
                link = res.headers['Location']
                return link
            except Exception as e:
                try:
                    if 'credentials' in res.json()['detail']:
                        self.logger.error('Login expired')
                        return None
                except:
                    self.logger.error(f'Failed to send alpha: {e}')
                    return None
            time.sleep(0.5)
                    