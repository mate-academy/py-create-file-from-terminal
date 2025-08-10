import sys
import os
from datetime import datetime


def main() -> None:
    command = sys.argv[1:]
    if "-d" in command:
        dir_index = command.index("-d")
        if "-f" in command:
            file_index = command.index("-f")
            dirs = command[dir_index + 1:file_index]
        else:
            dirs = command[dir_index + 1:]
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

    if "-f" in command:
        file_index = command.index("-f")
        file_path = command[file_index + 1]
        create_file(file_path)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line = 1
        while True:
            content = input("Input your content or enter 'stop': ")
            if content == "stop":
                break
            file.write(f"{line} Line{line} {content}" + "\n")
            line += 1
        file.write("\n")


if __name__ == "__main__":
    main()
