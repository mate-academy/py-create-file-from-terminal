from datetime import datetime
import os
import sys


def write_file(path: str) -> None:
    with open(path, "w") as file:
        now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        index = 1
        file.write(f"{now}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{index} Line {content}\n")
            index += 1


def create_dirs(args_list: str) -> str:
    file_index = args_list.index("-f")
    dirs_list = args_list[args_list.index("-d") + 1:file_index]
    dirs_path = os.path.join(*dirs_list)
    os.makedirs(dirs_path, exist_ok=True)
    file_name = args_list[file_index + 1]
    file_path = os.path.join(dirs_path, file_name)
    print(type(file_path))
    return file_path


if __name__ == "__main__":
    args = sys.argv
    if "-d" in args and "-f" in args:
        write_file(path=create_dirs(args))

    elif "-f" in args:
        write_file(path=args[-1])

    elif "-d" in args:
        dirs_path = os.path.join(*args[args.index("-d") + 1:])
        os.makedirs(dirs_path, exist_ok=True)
