import sys
import os
from datetime import datetime

def create_file():
    args = sys.argv[1:]
    

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for arg in args[d_index + 1:]:
            if arg == "-f":
                break
            path_parts.append(arg)
        dir_path = os.path.join(*path_parts) if path_parts else ""

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if file_name:
        full_path = os.path.join(dir_path, file_name)
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)


        with open(full_path, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            for index, line in enumerate(content_lines, start=1):
                f.write(f"{index} {line}\n")
            f.write("\n")

if __name__ == "__main__":
    create_file()
