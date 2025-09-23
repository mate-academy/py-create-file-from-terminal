import sys
import os
import datetime


def write_content_to_file(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    for i in range(len(lines)):
        lines[i] = f"{i + 1} " + lines[i]
    result = "\n".join(lines)
    with open(file_path, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                   + "\n")
        file.write(result)


if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        directories = sys.argv[d_index + 1: f_index]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        file_name = sys.argv[f_index + 1]
        write_content_to_file(os.path.join(path, file_name))
    else:
        directories = sys.argv[d_index + 1:]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    write_content_to_file(file_name)
