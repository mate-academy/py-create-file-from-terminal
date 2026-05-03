import os
import sys
from datetime import datetime


def create_file() -> None:
    i = 1
    dirs = []
    filename = None
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while (i < len(sys.argv)) and not sys.argv[i].startswith("-"):
                dirs.append(sys.argv[i])
                i += 1
            continue
        elif sys.argv[i] == "-f":
            filename = sys.argv[i + 1]
            i += 2
            continue
        i += 1

    path = os.path.join(*dirs) if dirs else ""
    if path:
        os.makedirs(path, exist_ok=True)

    full_path = os.path.join(path, filename)

    line_number = 1
    file_exists = os.path.exists(full_path)
    with open(full_path, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            file.write(f"{line_number}. {user_input}\n")

            line_number += 1
