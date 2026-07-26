import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = args[d_index + 1:]
        args = args[:d_index] + args[d_index + len(dir_path) + 1:]

    if "-f" in args:
        # Перевіряє, чи є флаг '-f' серед аргументів для вказання імені файлу.
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if dir_path:
        os.makedirs(os.path.join(*dir_path), exist_ok=True)

    if file_name:
        file_path = os.path.join(*dir_path, file_name) \
            if dir_path else file_name
        write_content_to_file(file_path)


def write_content_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []

    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as file:
        if os.stat(file_path).st_size != 0:
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")

    print(f"File '{file_path}' has been created/updated successfully.")


if __name__ == "__main__":
    main()
