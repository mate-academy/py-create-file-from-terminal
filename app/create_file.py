import os
import sys
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file_content = f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                file_content += "\n"
                break
            file_content += (user_input + "\n")
        file.write(file_content)


def create_directory() -> str:
    path = ""
    for element in range(2, len(sys.argv)):
        if sys.argv[element] == "-f":
            break
        path += sys.argv[element] + "/"
    os.makedirs(path.strip("/"), exist_ok=True)
    return path


if "-f" in sys.argv and "-d" in sys.argv:
    directory_path = create_directory() + sys.argv[-1]
    create_file(directory_path)
elif sys.argv[1] == "-d":
    create_directory()
elif sys.argv[1] == "-f":
    create_file(sys.argv[2])
