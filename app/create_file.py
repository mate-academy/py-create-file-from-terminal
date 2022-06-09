from datetime import datetime
from os import mkdir
from sys import argv as cmd


path = []

if cmd[1] == "-d":
    path = cmd[2:] if cmd[-2] != "-f" else cmd[2:-2]
    folder_name = f"{path[0]}"

    for i in range(len(path)):
        mkdir(folder_name)
        if i < len(path) - 1:
            folder_name += f"/{path[i + 1]}"


if cmd[-2] == "-f":
    f_path = f"{'/'.join(path)}/{cmd[-1]}" if cmd[1] == "-d" else f"{cmd[-1]}"

    with open(f_path, "a") as f:
        number_line = 1

        f.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "\n")

        while True:
            data = input("Enter content line: ")
            if data == 'stop':
                f.write("\n")
                break

            f.write(f"{number_line}. {data}\n")
            number_line += 1

print("Successful")
