import os
import argparse
import configparser
from utils import download_paper

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=int, default=0)
parser.add_argument('--id', type=str, default='')
parser.add_argument('--output', type=str, default='./')
parser.add_argument('--config', type=str, default='configs/config.ini')

args = parser.parse_args()

if args.mode == 0:
    download_paper(args.id, args.output)

elif args.mode == 1:
    config = configparser.ConfigParser()
    config.read(args.config)
    output = config['output']['dir'] + config['output']['subdir']
    
    for section in config.sections()[1:]:
        if section.startswith('paper:'):
            download_paper(config[section]['id'], output)