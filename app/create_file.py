import sys
import os
from datetime import datetime



def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_lines = []

    print("Enter content line (type 'stop' to finish):")
    line_number = 1
    while True:
        line = input(f"Enter content line: ")
        if line.lower() == "stop":
            break
        result_lines.append(f"{line_number} {line}")
        line_number += 1

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")
        file.write(timestamp + "\n")
        file.write("\n".join(result_lines) + "\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py -d [dir_path] -f [file_name]")
        return

    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = os.path.join(*args[d_index + 1:f_index])
        else:
            dir_path = os.path.join(*args[d_index + 1:])
            create_directory(dir_path)
            return

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if dir_path:
        create_directory(dir_path)
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    write_to_file(file_path)
    print(f"File '{file_path}' updated successfully.")


if __name__ == "__main__":
    main()
