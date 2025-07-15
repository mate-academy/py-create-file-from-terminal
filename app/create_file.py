import os
import sys
import datetime


def create_file_with_content(full_file_path: str) -> None:
    with open(full_file_path, "a") as new_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(timestamp + "\n")
        lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            lines.append(user_input)

        for number, line in enumerate(lines, start=1):
            new_file.write(f"{number} {line}\n")
        new_file.write("\n")


def create_directories(dirs_list: list) -> str:
    dir_path = os.path.join(*dirs_list)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    return dir_path


def parse_args():
    args = sys.argv[1:]

    dirs_list = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs_list.append(args[i])
                i += 1
            i -= 1
        elif args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
                i += 1
        i += 1

    return dirs_list, file_name


dirs_list, file_name = parse_args()

if dirs_list and file_name:
    dirs_path = create_directories(dirs_list)
    create_file_with_content(f"{dirs_path}/{file_name}")
elif dirs_list:
    create_directories(dirs_list)
elif file_name:
    create_file_with_content(file_name)
