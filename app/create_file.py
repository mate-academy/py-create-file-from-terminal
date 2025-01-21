import sys
import os
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    current_directory = os.getcwd()
    path = current_directory

    if "-d" in command:
        d_index = command.index("-d")
        directories = command[d_index + 1:]
        if "-f" in directories:
            directories = directories[:directories.index("-f")]
        path = os.path.join(current_directory, *directories)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory '{path}' created successfully")
        except OSError as error:
            print(f"Directory '{path}' cannot be created: {error}")

    if "-f" in command:
        f_index = command.index("-f")
        try:
            file_name = command[f_index + 1]
            file_path = os.path.join(path, file_name)

            with open(file_path, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\n{timestamp}\n")

                line_number = 1
                while True:
                    content = input(f"Enter content line ({line_number}): ")
                    if content.lower() == "stop":
                        break
                    file.write(f"{line_number} {content}\n")
                    line_number += 1

            print(f"File created/updated: {file_path}")
        except IndexError:
            print("Error: No file name provided after '-f'")
        except Exception as e:
            print(f"Error while creating file: {e}")
