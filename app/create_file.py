import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs = []
file_name = None
new_file = None

for i in args:
    if i == "-d":
        new_file = "-d"
    elif i == "-f":
        new_file = "-f"
    else:
        if new_file == "-d":
            dirs.append(i)
        elif new_file == "-f":
            file_name = i

if dirs:
    new_fille = os.path.join(*dirs)
    os.makedirs(new_fille, exist_ok=True)

if file_name is not None:
    full_path = os.path.join(*dirs, file_name)
    file_exists = os.path.exists(full_path)
    new_files = []

    while True:
        file_dir = input("Enter content line: ")
        if file_dir == "stop":
            break
        else:
            new_files.append(file_dir)

    times = datetime.now()
    new_times = times.strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    for number, new_number in enumerate(new_files, start=1):
        lines.append(f"{number} {new_number}")
    numbers = "\n".join(lines)
    new_numbers = new_times + "\n" + numbers

    if file_exists:
        exis = "\n\n" + new_numbers
    else:
        exis = new_numbers

    with open(full_path, "a") as new_exis:
        new_exis.write(exis)
