import datetime
import os
import sys


def write_to_file(filepath: str) -> None:
    file_exists = os.path.exists(filepath) and os.path.getsize(filepath) > 0

    with open(filepath, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{line} {user_input}\n")
            line += 1


command = sys.argv

# 1. Guard against missing CLI arguments
if len(command) < 2:
    print("Usage: python script.py [-d dir1 ...] [-f file.txt]")
    sys.exit(1)

command_tag = command[1]

if "-f" in command and "-d" in command:
    d_idx = command.index("-d")
    f_idx = command.index("-f")

    names = []
    if d_idx < f_idx:
        for i in range(d_idx + 1, f_idx):
            names.append(command[i])
    elif d_idx > f_idx:
        for i in range(d_idx + 1, len(command)):
            names.append(command[i])

    full_dir_path = os.path.join(*names)
    os.makedirs(full_dir_path, exist_ok=True)

    # Validate that a filename exists after the -f flag
    if f_idx + 1 < len(command):
        trg_file = os.path.join(full_dir_path, command[f_idx + 1])
        write_to_file(trg_file)
    else:
        print("Error: Missing filename after -f flag.")
        sys.exit(1)

elif command_tag == "-d":
    names = []
    for i in range(2, len(command)):
        names.append(command[i])

    if names:
        full_dir_path = os.path.join(*names)
        os.makedirs(full_dir_path, exist_ok=True)

elif command_tag == "-f":
    if len(command) > 2:
        trg_file = command[2]
        write_to_file(trg_file)
    else:
        print("Error: Missing filename after -f flag.")
        sys.exit(1)
