import os
import sys
from datetime import datetime


def get_file_content() -> str:
    text = ""
    line = 1
    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        text += f"{line} {content}\n"
        line += 1
    return text


def create_file(file_name: str, text: str) -> None:
    with open(file_name, "a") as file_out:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_out.write(f"{time_now}\n{text}")


def create_dirs(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_dirs_and_file(path: str,
                         file_name: str,
                         text: str) -> None:
    os.makedirs(path, exist_ok=True)
    create_file(os.path.join(path, file_name), text)


def main() -> None:
    com_line = sys.argv
    if "-d" in com_line and "-f" in com_line:
        dirs = com_line[com_line.index("-d") + 1:com_line.index("-f")]
        path = os.path.join(*dirs)
        create_dirs_and_file(path, com_line[-1], get_file_content())
    elif "-f" in com_line:
        create_file(com_line[-1], get_file_content())
    elif "-d" in com_line:
        dirs = com_line[com_line.index("-d") + 1:]
        path = os.path.join(*dirs)
        create_dirs(path)


if __name__ == "__main__":
    main()
