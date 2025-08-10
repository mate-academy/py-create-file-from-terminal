import os
import sys
from datetime import datetime


def create_directory(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")


def create_file(filepath: str) -> None:
    try:
        with open(filepath, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")
            print(f"File '{filepath}' created/updated."
                  f" Please enter the file content"
                  f" (type 'stop' to finish): ")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py"
              " [-d path_parts...]"
              " | [-f filename]"
              " | [-d path_parts... -f filename]")
        return
    flag_d = "-d" in sys.argv
    flag_f = "-f" in sys.argv
    if flag_d and flag_f:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        if d_index < f_index:
            path_parts = sys.argv[d_index + 1:f_index]
            filename = sys.argv[f_index + 1]
        if d_index > f_index:
            path_parts = sys.argv[d_index + 1:]
            filename = sys.argv[2]
        dir_path = os.path.join(*path_parts)
        create_directory(path_parts)
        create_file(os.path.join(dir_path, filename))
    elif flag_d:
        d_index = sys.argv.index("-d")
        path_parts = sys.argv[d_index + 1:]
        create_directory(path_parts)
    elif flag_f:
        f_index = sys.argv.index("-f")
        filename = sys.argv[f_index + 1]
        create_file(filename)
    else:
        print("Invalid flag. Use -d for directory or -f for file.")
        print("Usage: python create_file.py"
              " [-d path_parts...]"
              " | [-f filename]"
              " | [-d path_parts... -f filename]")


if __name__ == "__main__":
    main()
