import os
import sys

import datetime

command_arguments = sys.argv

if command_arguments:
    path = ""
    file_name = ""
    for command_arguments_index in range(0, len(command_arguments)):

        if command_arguments[command_arguments_index] == "-d":
            for directories_index in range(
                    command_arguments_index + 1,
                    len(command_arguments)
            ):
                if command_arguments[directories_index] == "-f":
                    command_arguments_index = directories_index
                    break
                path = os.path.join(path, command_arguments[directories_index])

        if command_arguments[command_arguments_index] == "-f":
            file_name = command_arguments[command_arguments_index + 1]

    if path:
        os.makedirs(path, exist_ok=True)
        print(f"Created a directory: {path}")
    if file_name:
        new_file = os.path.join(path, file_name)
        with open(new_file, "w") as file:
            file.write(f"{(datetime.datetime.now())
                       .strftime("%Y-%m-%d %H:%M:%S")}\n")
            line_counter = 1
            while True:
                print(f"Enter content line №{line_counter}: ")
                command = input()
                if command.lower() == "stop":
                    break
                file.write(command)
                line_counter += 1
