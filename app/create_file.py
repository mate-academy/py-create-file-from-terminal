import sys
from datetime import datetime
import os.path


def write_file(name: str) -> None:
    now = datetime.now()
    user_input = ""
    res = f'{now.strftime("%Y-%m-%d %H:%M:%S")}\n'
    line_number = 1

    while user_input != "stop":
        user_input = input("Enter content line: ")
        if user_input != "stop":
            res += f"{line_number} {user_input}\n"
            line_number += 1

    if os.path.exists(name):
        res = "\n" + res

    with open(name, "a") as f:
        f.write(res)


def create_file() -> None:
    args = sys.argv[1:]
    directories = []
    file_name = None

    for i, arg in enumerate(args):
        if arg == "-f":
            file_name = args[i + 1]
        elif arg == "-d":
            for dir_name in range(i + 1, len(args)):
                if args[dir_name] == "-f":
                    break
                directories.append(args[dir_name])

    directory_path = ""
    if len(directories) != 0:
        directory_path = os.path.join(*directories)
        print(directory_path)
        os.makedirs(directory_path, exist_ok=True)
    if file_name:
        write_file(os.path.join(directory_path, file_name))


if __name__ in ("__main__", "<run_path>"):
    create_file()
