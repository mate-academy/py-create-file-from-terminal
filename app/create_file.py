import sys
import os
import datetime


datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
command_parts = sys.argv

if "-f" in command_parts:
    file_name = command_parts[command_parts.index("-f") + 1]

    if "-d" in command_parts:
        dir_parts = command_parts[
            command_parts.index("-d") + 1:command_parts.index("-f")
        ]
        dir_path = "/".join(dir_parts)
        os.makedirs(dir_path, exist_ok=True)
        file_path = f"{dir_path}/{file_name}"
    else:
        file_path = file_name
    with open(file_path, "a") as file:
        file.write(f"{datetime_now}\n")
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{line_number} {text}\n")
elif "-d" in command_parts:
    dir_parts = command_parts[command_parts.index("-d") + 1:]
    dir_path = "/".join(dir_parts)
    os.makedirs(dir_path, exist_ok=True)
