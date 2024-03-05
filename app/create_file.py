import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    if directory:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
    else:
        filepath = filename

    if os.path.exists(filepath):
        mode = 'a'
    else:
        mode = 'w'

    with open(filepath, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        line_number = 1
        while True:
            content_line = input("Enter content line (or 'stop' to finish): ")
            if content_line.lower() == 'stop':
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


if len(sys.argv) == 1:
    print("Usage: python create_file.py -d directory_path -f filename")
    sys.exit(1)

if '-d' in sys.argv:
    directory_index = sys.argv.index('-d') + 1
    directory = os.path.join(*sys.argv[directory_index:])
    filename = None
elif '-f' in sys.argv:
    filename_index = sys.argv.index('-f') + 1
    directory = None
    filename = sys.argv[filename_index]
else:
    print("Invalid arguments. Use either -d or -f flag.")
    sys.exit(1)

create_file(directory, filename)
