from datetime import datetime
import os
import sys


def create_file_inside_directory() -> None:
    cmd_list = sys.argv
    path = ""
    if "-d" in cmd_list:
        if "-f" in cmd_list:
            path = os.path.join(*(cmd_list[2:-2]))
        else:
            path = os.path.join(*(cmd_list[2::]))
        if path:
            os.makedirs(path, exist_ok=True)
    if "-f" in cmd_list:
        with open(os.path.join(path, cmd_list[-1]), "a") as new_file:
            new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            while True:
                content_line = input("Enter content line:")
                if content_line != "stop":
                    new_file.write(f"{content_line}\n")
                else:
                    break


if __name__ == "__main__":
    create_file_inside_directory()
