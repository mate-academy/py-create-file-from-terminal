import os
import sys
from datetime import datetime


def create_file(filename: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, filename), "a") as file:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        file.write(data)
        while True:
            user_line = input("Enter content line: ") + "\n"
            if user_line == "stop":
                break
            file.write(user_line)
        file.write("\n")


def create_directory(file_path: list[str]) -> str:
    path = os.path.join(*file_path)
    os.makedirs(path, exist_ok=True)
    return path


def main() -> None:
    argv = sys.argv
    if "-d" in argv and "-f" not in argv:
        filename = argv[argv.index("-f") + 1]
        path = create_directory(
            argv[argv.index("-d") + 1: argv.index("-f")]
        )
        create_file(filename=filename, path=path)

    if "-d" in argv:
        create_directory(argv[argv.index("-d") + 1:])

    if "-f" in argv:
        create_file(filename=argv[argv.index("-f") + 1])


if __name__ == "__main__":
    create_directory(["dir1", "dir2"])
    create_file("new_file", "dir1/dir2/")
    main()
