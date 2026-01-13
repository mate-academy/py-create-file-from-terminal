import sys
import os
from datetime import datetime

print(sys.argv)

def create_file() -> None:
    command = sys.argv
    folder_path = ""
    if command[1] == "-d":
        if "-f" in command:
            f_index = command.index("-f")
            dir_parts = command[2 : f_index]
            folder_path = os.path.join(*dir_parts)
            os.makedirs(folder_path, exist_ok=True)
            file_name = command[f_index + 1]
            full_path = os.path.join(folder_path, file_name)
            content_creating(full_path)
        else:
            dir_parts = command[2:]
            folder_path = os.path.join(*dir_parts)
            os.makedirs(folder_path, exist_ok=True)
    elif command[1] == "-f":
        content_creating(command[2])


def content_creating(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        count = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(str(count) + " " + content + "\n")
            count += 1
        f.write("\n")
create_file()

