import logging
import requests
import json
import os 
import time 
import argparse
import dotenv
dotenv.load_dotenv(".env")

from configs.log_config import LogConfig
from packages.engines.WorldQuant_Engine import WorldQuantEngine

def parser_args():
    parse = argparse.ArgumentParser(description='WQBrain')
    parse.add_argument('--email', type=str, default = os.getenv("EMAIL"), required=False, help='Email for login')
    parse.add_argument('--password', type=str, default = os.getenv("PASSWORD"), required=False, help='Password for login')
    parse.add_argument('--log_dir', type=str, default = os.getenv("LOG_DIR"), required=False, help='Log directory')
    parse.add_argument('--alpha_name', type=str, default = "WQBrain", required=False, help='Alpha name')
    
    return parse.parse_args()


if __name__ == "__main__":
    args = parser_args()
    log_config = LogConfig(
        log_name = args.alpha_name,
        log_dir = args.log_dir,
        log_level = logging.INFO,
        propagate = False
    )
    engine = WorldQuantEngine(args.email, args.password, log_config)