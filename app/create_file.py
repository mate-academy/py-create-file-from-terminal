from datetime import datetime
from sys import argv
from os import makedirs

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
command = argv
dirs_path = []
line_n = 1

if "-d" in command:
    for i in range(command.index("-d") + 1, len(command)):
        if command[i] == "-f":
            break
        dirs_path.append(command[i])

    try:
        makedirs(f"./{'/'.join(dirs_path)}")
    except FileExistsError:
        pass

if "-f" in command and command.index("-f") < len(command) - 1:
    file_name = command[command.index("-f") + 1]

    if len(dirs_path) > 0:
        file_path = f"{'/'.join(dirs_path)}/{file_name}"
    else:
        file_path = file_name

    with open(file_path, "a") as file:
        file.write(now + "\n")

        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                file.write("\n")
                break
            else:
                file.write(f"{line_n} {new_line}\n")
                line_n += 1
