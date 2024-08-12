# write your code here
from datetime import datetime
import sys
import os


def create_directory(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def create_in_file(file: str) -> None:
    with open(file, 'w') as f:
        f.write(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
        line_numbers = 0

        while True:
            input_user = input("Enter content line: ")
            if input_user == "stop":
                f.write("\n")
                break
            line_numbers += 1
            f.write(f"{line_numbers} {input_user}\n")


def parse_args(args: list) -> dict:
    new_dict = {"-d": [], "-f": None}
    i = 0
    while i < len(args):
        if args[i] == '-f':
            if i + 1 < len(args):
                new_dict['-f'] = args[i + 1]
                i += 1
        elif args[i] == '-d':
            j = i + 1
            while j < len(args) and not args[j].startswith('-'):
                new_dict['-d'].append(args[j])
                j += 1
            i = j - 1
        i += 1

    return new_dict


def main() -> None:
    directories, file_name = parse_args(sys.argv[1:])

    if file_name and directories:
        create_directory(directories)
        full_name = os.path.join(*directories, file_name)
        create_in_file(full_name)
    elif file_name:
        create_in_file(file_name)
    elif directories:
        create_directory(directories)


if __name__ == '__main__':
    main()
