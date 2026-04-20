import os
import sys
from datetime import datetime


def create_directories(path: str) -> str:
    directories = path.split("/")
    full_dir = ""
    for i in range(len(directories)):
        if directories[i] == "-f":
            break
        full_dir += directories[i] + "/"
        if not os.path.exists(full_dir):
            os.mkdir(full_dir)
    return full_dir


def write_to_file(path: str, data: str) -> None:
    with open(path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        f.write(data + "\n")


def main() -> None:
    dirs = ""
    if sys.argv[1] == "-d":
        dirs = create_directories("/".join(sys.argv[2:]))
    if "-f" in sys.argv:
        text = ""
        while True:
            user_command = input("Enter new line of content: ")
            if user_command == "stop":
                break
            text += user_command + "\n"

        path = dirs + sys.argv[len(sys.argv) - 1]
        write_to_file(path, text)


if __name__ == "__main__":
    main()
