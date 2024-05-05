import os
import time
import logging
from typing import Literal, get_args
from datetime import datetime
from configs.log_config import LogConfig


class BaseLogger:
    def __init__(self, log_config: LogConfig):
        self.logger = logging.getLogger(log_config.log_name)

        # log config
        self.log_config = log_config
        self.log_dir = log_config.log_dir
        self.log_name = log_config.log_name
        self.log_level = log_config.log_level
        self.log_file_path = os.path.join(self.log_dir, f"{self.log_name}.log")

        # formatter
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # setting for outputing to stdout or not
        self.logger.propagate = log_config.propagate

        # make dirs
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # update logger
        self.update_logger()

    def get_logger(self):
        return self.logger

    def get_current_timestamp(self):
        return datetime.now().timestamp()

    def create_log_handler(
        self, log_type: Literal["info", "err"]
    ) -> logging.FileHandler:
        filename = f"{self.log_name}.{log_type}.log"
        filepath = os.path.join(self.log_dir, filename)
        log_file_handler = logging.FileHandler(filepath, encoding="utf-8")
        if log_type == "info":
            level = logging.INFO
        else:
            level = logging.WARNING
        log_file_handler.setLevel(level)
        log_file_handler.setFormatter(self.formatter)
        return log_file_handler

    def update_logger(self):
        self.logger.setLevel(self.log_level)
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)
        for state_type in get_args(Literal["info", "err"]):
            handler = self.create_log_handler(state_type)
            self.logger.addHandler(handler)