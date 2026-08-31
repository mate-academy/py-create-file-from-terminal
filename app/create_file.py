import datetime
import os
import sys


def create_file() -> None:
    command = sys.argv[1:]

    # Finding indexes for commands
    f_index = command.index("-f") if "-f" in command else None
    d_index = command.index("-d") if "-d" in command else None

    # Trying to parse file name from command
    file_name = None
    if f_index is not None:
        file_name = command[f_index + 1]

    # Trying to parse directories from command
    directory_path = None
    if d_index is not None:
        if not file_name or f_index < d_index:
            directory_path = os.path.join(*command[d_index + 1:])
        else:
            directory_path = os.path.join(*command[d_index + 1:f_index])

    # Creating files if needed
    if directory_path:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        if file_name:
            file_name = os.path.join(directory_path, file_name)

    # Creating or opening file if needed
    if file_name:
        with open(file_name, "a") as new_file:
            if os.path.getsize(file_name) != 0:
                new_file.write("\n")
            now = datetime.datetime.now()
            new_file.write(now.strftime("%Y-%m-%d %X\n"))
            num = 1
            while True:
                user_input = input("Enter content line: ")
                if user_input.lower() == "stop":
                    break
                new_file.write(f"{num} {user_input}\n")
                num += 1


create_file()
