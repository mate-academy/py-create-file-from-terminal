import os
import datetime
import sys


def create_directory() -> str:
    parent_dir = os.getcwd()
    directory = (
        sys.argv[2:sys.argv.index("-f")]
        if "-f" in sys.argv
        else sys.argv[2:]
    )
    path = os.path.join(parent_dir, *directory)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"New directory created at {path}")
    else:
        print(f"Directory already exists at {path}")
    return path


def create_file(dir_path: str) -> None:
    file_path = os.path.join(dir_path, sys.argv[sys.argv.index("-f") + 1])
    counter = 1
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) == 0:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        else:
            f.write(datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S\n"))
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            f.write(f"{counter} {user_input}\n")
            counter += 1
    if os.path.exists(file_path):
        print(f"File updated at {file_path}")
    else:
        print(f"New file created at {file_path}")


if "-d" in sys.argv and "-f" in sys.argv:
    directory_path = create_directory()
    create_file(directory_path)
elif sys.argv[1] == "-d":
    create_directory()
elif sys.argv[1] == "-f":
    create_file(os.getcwd())
