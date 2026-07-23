import os
import sys
import datetime


def write_content(file_path: str) -> None:
    with open(file_path, "a") as new_file:
        counter = 1
        today = datetime.datetime.now()
        timestamp = today.strftime("%Y-%m-%d %H:%M:%S")

        if os.path.getsize(file_path) != 0:
            new_file.write("\n")
        new_file.write(str(timestamp) + "\n")

        while True:
            text = input("Enter content line: ")
            if not text or text.lower() == "stop":
                break
            new_file.write(f"{counter} {text}\n")
            counter += 1


if len(sys.argv) < 3:
    sys.exit(1)
flag = sys.argv[1]
both_flags = sys.argv
if "-f" in both_flags and "-d" in both_flags:
    f_index = sys.argv.index("-f")
    d_index = sys.argv.index("-d")

    if f_index > d_index:
        dir_parts = sys.argv[2:f_index]
        file_name = sys.argv[f_index + 1]

    elif f_index < d_index:
        file_name = sys.argv[f_index + 1]
        dir_parts = sys.argv[d_index + 1:]

    current_path = ""
    for part in dir_parts:
        current_path = os.path.join(current_path, part)

    os.makedirs(current_path, exist_ok=True)
    file_path = os.path.join(current_path, file_name)
    write_content(file_path)

elif flag == "-d":
    current_path = ""

    for part in sys.argv[2:]:
        current_path = os.path.join(current_path, part)
    os.makedirs(current_path, exist_ok=True)

elif flag == "-f":
    file_name = sys.argv[2]
    write_content(file_name)
