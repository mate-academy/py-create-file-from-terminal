import sys
import os
from datetime import datetime


def create_file() -> None:
    if '-d' in sys.argv:
        dir_index = sys.argv.index('-d')
        dir_path = '/'.join(sys.argv[dir_index + 1:])
        os.makedirs(dir_path, exist_ok=True)
    if '-f' in sys.argv:
        file_index = sys.argv.index('-f')
        file_name = sys.argv[file_index + 1]
        file_path = f'{dir_path}/{file_name}' if '-d' in sys.argv else file_name
        with open(file_path, 'a') as file:
            file.write(f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            line_number = 0
            while True:
                line = input('Enter content line: ')
                if line == 'stop':
                    break
                line_number += 1
                file.write(f'\n{line_number} {line}')
