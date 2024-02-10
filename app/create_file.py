import os
import sys
from datetime import datetime


def create_file(file_p: str) -> None:
    todays_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_p, 'w') as f:
        f.write(f'{todays_date}\n')
        line = 1
        while True:
            new_line = input('Enter new line of content: ')
            if new_line.lower() == 'stop':
                break
            f.write(f'{line} {new_line}\n')
            line += 1


def create_dir(path: str) -> str:
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def main() -> None:
    if '-d' in sys.argv and '-f' in sys.argv:
        path = '/'.join(sys.argv[2:-2])
        create_dir(path)
        create_file(f'{path}/{sys.argv[-1]}')
    elif '-d' in sys.argv:
        create_dir('/'.join(sys.argv[2:-2]))
    elif '-f' in sys.argv:
        create_file(sys.argv[-1])


if __name__ == '__main__':
    main()
