import os
import sys

from datetime import datetime


command = sys.argv

if "-d" in command and "-f" not in command:
    directory_path = os.path.join("/".join(command[command.index("-d") + 1:]))
    os.makedirs(directory_path, exist_ok=True)

if "-f" in command:
    file_name = command[command.index("-f") + 1]

    if "-d" in command:
        index_of_f, index_of_d = command.index("-f"), command.index("-d")
        file_name = command[index_of_f + 1]
        directory_path = os.path.join(
            "/".join(command[index_of_d + 1:index_of_f])
        )
        file_path = os.path.join(directory_path, file_name)

    else:
        file_path = os.path.join(os.getcwd(), file_name)

    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 0

        while True:
            line_content = input("Enter content line: ")
            line_number += 1

            if line_content == "stop":
                file.write("\n")
                break

            file.write(f"{line_number} {line_content}\n")
