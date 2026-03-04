import sys
import os
from datetime import datetime
from typing import List, Optional


def get_timestamp() -> str:
    # Return current timestamp formatted as YYYY-MM-DD HH:MM:SS
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def read_content_from_terminal() -> List[str]:
    # Read lines from user until "stop" is entered
    lines: List[str] = []
    line_number = 1

    while True:
        user_input = input('Enter content line: ')

        if user_input.lower() == 'stop':
            break

        lines.append(f'{line_number} {user_input}')
        line_number += 1

    return lines


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print('No arguments provided.')
        return

    directory_parts: List[str] = []
    file_name: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == '-d':
            i += 1
            while i < len(args) and args[i] not in ('-d', '-f'):
                directory_parts.append(args[i])
                i += 1

        elif args[i] == '-f':
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print('File name not provided after -f flag.')
                return
        else:
            print(f'Unknown argument: {args[i]}')
            return

    target_directory = os.getcwd()

    if directory_parts:
        target_directory = os.path.join(
            os.getcwd(),
            *directory_parts,
        )
        os.makedirs(target_directory, exist_ok=True)

    if file_name:
        file_path = os.path.join(target_directory, file_name)

        content_lines = read_content_from_terminal()

        if not content_lines:
            print('No content provided.')
            return

        timestamp = get_timestamp()

        file_exists = os.path.exists(file_path)
        mode = 'a' if file_exists else 'w'

        with open(file_path, mode, encoding='utf-8') as file:
            if file_exists:
                file.write('\n')

            file.write(f'{timestamp}\n')

            for line in content_lines:
                file.write(f'{line}\n')

        print(f'File created/updated at: {file_path}')


if __name__ == '__main__':
    main()
