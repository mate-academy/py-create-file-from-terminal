import os
import sys

import datetime

command_arguments = sys.argv[1:]

if len(command_arguments) > 1:
    path = ""
    file_name = ""
    for command_arguments_index in range(0, len(command_arguments)):

        if command_arguments[command_arguments_index] == "-d":
            if (command_arguments_index + 1) < len(command_arguments):
                for directories_index in range(
                        command_arguments_index + 1,
                        len(command_arguments)
                ):
                    if command_arguments[directories_index] == "-f":
                        command_arguments_index = directories_index
                        break
                    path = os.path.join(
                        path,
                        command_arguments[directories_index]
                    )

        if command_arguments[command_arguments_index] == "-f":
            if (command_arguments_index + 1) < len(command_arguments):
                file_name = command_arguments[command_arguments_index + 1]

    if path != "":
        os.makedirs(path, exist_ok=True)
        print(f"Created a directory: {path}")
    if file_name:
        new_file = os.path.join(path, file_name)
        with open(new_file, "a") as file:
            file.write(
                f"{(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")}\n")
            line_counter = 1
            while True:
                print(f"Enter content line №{line_counter}: ")
                command = input()
                if command.lower() == "stop":
                    file.write("\n")
                    break
                file.write(f"{line_counter} {command}")
                line_counter += 1
