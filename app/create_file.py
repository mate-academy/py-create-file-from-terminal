import os
import sys
from datetime import datetime


def main() -> None:
    directory_path = ""
    file_path = ""
    create_directory = False
    create_file = False
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            directory_parts = []
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
            if directory_parts:
                directory_path = os.path.join(*directory_parts)
                create_directory = True
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_path = args[i]
                create_file = True
                break
            i += 1

    if create_directory and directory_path:
        os.makedirs(directory_path, exist_ok=True)
    if create_file and file_path:
        full_file_path = os.path.join(directory_path, file_path) if directory_path else file_path
        with open(full_file_path, "a") as result_file:
            content = []
            current_date = datetime.now()
            content.append(current_date.strftime("%Y-%m-%d %H:%M:%S"))
            print("Enter content lines (type 'stop' to finish)")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                content.append(f"{line_number} line {line}")
                line_number += 1
            result_file.write("\n".join(content) + "\n")


if __name__ == "__main__":
    main()
