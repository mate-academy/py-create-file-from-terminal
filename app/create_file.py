import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    has_d = "-d" in args
    has_f = "-f" in args
    path_to_create: str = ""
    if has_d:
        d_index = args.index("-d")
        end_index = len(args)
        if has_f and args.index("-f") > d_index:
            end_index = args.index("-f")
        dir_parts = args[d_index + 1:end_index]
        if dir_parts:
            path_to_create = os.path.join(*dir_parts)
            os.makedirs(path_to_create, exist_ok=True)
    if has_f:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
            full_file_path = file_name
            if path_to_create:
                full_file_path = os.path.join(path_to_create, file_name)
            content_lines = []
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                content_lines.append(line)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text_to_write = f"{timestamp}\n"
            for i, line in enumerate(content_lines, 1):
                text_to_write += f"{i} {line}\n"
            with open(full_file_path, "a", encoding="utf-8") as f:
                f.write(text_to_write)
