import os
import argparse
import configparser
from utils import preprocess_id

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='configs/sample.ini')
parser.add_argument('--output', type=str, default='./')
parser.add_argument('--subdir', type=str, default='')
args = parser.parse_args()

if os.path.exists(args.config):
    print(f'Config file {args.config} already exists. Overwrite? (y/n)')
    overwrite = input()
    if overwrite.lower() != 'y':
        print('Exiting...')
        exit(0)
    else:
        os.system(f'rm {args.config}')

print("please type in arxiv id or link")
# new a config file
config = configparser.ConfigParser()
config['output'] = {'dir': args.output, 'subdir': args.subdir}
# keep reading input until EOF
cur_id = 0
while True:
    try:
        # read the input
        line = input()
        # parse the input
        new_line = preprocess_id(line)
        if new_line is None:
            print('Invalid paper ID ' + line)
            continue
        # add the new line to the config file
        config['paper:' + str(cur_id)] = {'id': new_line}
        cur_id += 1
    except EOFError:
        break
with open(args.config, 'w') as configfile:
    config.write(configfile)