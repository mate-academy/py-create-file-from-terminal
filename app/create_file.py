import sys
import datetime
import os


def create_file() -> None:
    index = sys.argv.index("-f") + 1
    file_name = sys.argv[index]
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_parts = sys.argv[dir_index: sys.argv.index("-f")]
        parent_path = os.getcwd()
        dir_path = os.path.join(parent_path, *dir_parts)
        full_file_path = os.path.join(dir_path, file_name)
    else:
        full_file_path = os.path.join(os.getcwd(), file_name)
    with open(full_file_path, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{i} " + line + "\n")
            i += 1


def create_directory() -> None:
    directory = []
    parent_path = os.getcwd()
    for i in range(2, len(sys.argv)):
        if sys.argv[i] == "-f":
            break
        directory.append(sys.argv[i])
    path = os.path.join(parent_path, *directory)
    os.makedirs(path, exist_ok=True)


if sys.argv[1] == "-f":
    create_file()


if sys.argv[1] == "-d":
    create_directory()


if "-f" in sys.argv and "-d" in sys.argv:
    create_directory()
    create_file()
