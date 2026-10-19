import sys
import os
import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None
    if "-d" in args:
        d_index = args.index("-d")
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
    dir_path = os.path.join(*dir_parts) if dir_parts else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if not file_name:
        return
    full_path = os.path.join(dir_path, file_name) if dir_path else file_name
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    formated_content = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    for indx, line in enumerate(content_lines, start=1):
        formated_content.append(f"{indx} {line}")

    with open(full_path, "a+") as f:
        f.seek(0)
        full_file = f.read()
        if full_file:
            f.write("\n")
        f.write("\n".join(formated_content) + "\n")


create_file()
