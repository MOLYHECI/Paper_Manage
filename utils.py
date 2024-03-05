import os
import re

arxiv_patterns = [
    '([0-9]+\.[0-9]+)',
    'arxiv:([0-9]+\.[0-9]+)',
    'arxiv.org/abs/([0-9]+\.[0-9]+)',
    'https://arxiv.org/abs/([0-9]+\.[0-9]+)',
    'arxiv.org/pdf/([0-9]+\.[0-9]+).pdf',
    'https://arxiv.org/pdf/([0-9]+\.[0-9]+).pdf',
]
def preprocess_id(id):
    for pattern in arxiv_patterns:
        match = re.search(pattern, id)
        if match:
            return match.group(1)
    return None

def download_paper(id: str, output: str):
    new_id = preprocess_id(id)
    if new_id is None:
        print('Invalid paper ID ' + id)
        return

    # Create the output directory if it does not exist
    os.makedirs(output, exist_ok=True)
    print(f'Downloading paper {new_id} to {output}')
    # Download the paper
    command = f'curl --max-time 10 -o {output}/{new_id}.pdf https://arxiv.org/pdf/{new_id}.pdf'
    # Check the return value of curl
    max_attempts = 10
    while os.system(command) != 0 and max_attempts > 0:
        print('Download failed. Retrying...')
        max_attempts -= 1
    if max_attempts == 0:
        print(f'Download {new_id} failed after 10 attempts. Skipping...')
        return False
    print(f'Download {new_id} complete.')
    return True
