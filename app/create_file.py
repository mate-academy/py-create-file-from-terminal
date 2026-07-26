from datetime import datetime
import os
import sys


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_file() -> None:
    file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    line = 1

    with open(sys.argv[-1], "a") as file_out:
        file_out.write(file_content)
        while True:
            file_content = input("Enter file_content line: ")
            if file_content == "stop":
                file_out.write("\n")
                break
            file_out.write(f"{line} {file_content}\n")
            line += 1


def create_directory(file_name: str = None) -> None:
    path = sys.argv[2:-2] if file_name else sys.argv[2:]
    path = create_path(path)

    os.makedirs(path, exist_ok=True)

    if file_name:
        os.chdir(path)
        create_file()


if __name__ == "__main__":
    create_file()
