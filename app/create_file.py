import os
import sys
from datetime import datetime


def create_directory(path_parts: str | list) -> str:
    full_path = os.path.join(os.getcwd(), *path_parts)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def write_to_file(file_path: str, content_lines: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{timestamp}\n")
        for index, line in enumerate(content_lines, 1):
            f.write(f"{index} {line}\n")
        f.write("\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dirs] [-f filename]")
        sys.exit(1)
    dirs = []
    file_name = None
    flag_d = False
    flag_f = False
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            flag_d = True
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                dirs.append(sys.argv[i])
                i += 1
        elif sys.argv[i] == "-f":
            flag_f = True
            i += 1
            if i < len(sys.argv):
                file_name = sys.argv[i]
            i += 1
        else:
            i += 1
    if flag_d:
        if not dirs:
            print("Error: Missing directory path after -d.")
            sys.exit(1)
        create_directory(dirs)
    if flag_f:
        if not file_name:
            print("Error: Missing file name after -f.")
            sys.exit(1)
        if flag_d:
            file_path = os.path.join(os.getcwd(), *dirs, file_name)
        else:
            file_path = os.path.join(os.getcwd(), file_name)
        print(f"Enter content for {file_path}. Type 'stop' to finish: ")
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)
        write_to_file(file_path, content_lines)
        print(f"Content written to {file_path}.")


if __name__ == "__main__":
    main()
