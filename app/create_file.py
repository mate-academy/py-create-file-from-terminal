import sys
import os
from datetime import datetime


def create_file(file_path: str = f"app/{sys.argv[-1]}") -> None:
    request = sys.argv
    if len(request) <= 3:
        print("File name not provided.")
        return
    with open(file_path, "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_idx = 1
        content = ""
        while content != "stop":
            content = input("Enter content line: ")
            file.write(f"{line_idx} {content}\n")
            line_idx += 1
    print(f"Created file: {request[-1]}")


def create_directory() -> None | str:
    request = sys.argv
    if len(request) < 3:
        print("Directory path not provided.")
        return
    directory = os.path.join(*request[2:])
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")
    return directory


def create_directory_and_file() -> None:
    request = sys.argv
    if len(request) < 5 and request[-2] != "-f":
        print("Incorrect call")
        return
    directory = os.path.join(*request[2:-2])
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")
    file_path = f"{directory}/{request[-1]}"
    create_file(file_path)


def main() -> None:
    request = sys.argv
    if len(request) == 1:
        print("Incorrect call")
        return
    if request[1] == "-d" and "-f" not in request:
        create_directory()
    if request[1] == "-f":
        create_file()
    if request[1] == "-d" and "-f" in request:
        create_directory_and_file()


if __name__ == "__main__":
    main()
