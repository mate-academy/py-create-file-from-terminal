from datetime import datetime
import os
import sys


def create_directory(command: str) -> str:
    path = ""
    if "-d" in command:
        if "-f" in command:
            path = os.path.join(*(command[2:-2]))
        else:
            path = os.path.join(*(command[2::]))
        if path:
            os.makedirs(path, exist_ok=True)
    return path


def create_file(command: str, path: str) -> None:
    if "-f" in command:
        content_lines = []
        while True:
            content_line = input("Enter content line:")
            if content_line == "stop":
                break
            content_lines.append(content_line + "\n")
            print(content_lines)
        with open(os.path.join(path, command[-1]), "a") as new_file:
            new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for line in content_lines:
                new_file.write(line)


def create_file_inside_directory() -> None:
    cmd_list = sys.argv
    path = create_directory(cmd_list)
    print("path: ", path)
    create_file(cmd_list, path)


if __name__ == "__main__":
    create_file_inside_directory()
