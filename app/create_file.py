import os
import sys
from datetime import datetime


def main() -> None:
    if "-d" not in sys.argv and "-f" not in sys.argv:
        print("Usage: python create_file.py [-d <directories>] -f <file_name>")
        sys.exit(1)

    directories = []
    file_name = None
    file_path = None

    if "-d" in sys.argv:
        index_d = sys.argv.index("-d") + 1
        for arg in sys.argv[index_d:]:
            if arg == "-f":
                break
            directories.append(arg)

    if "-f" in sys.argv:
        index_f = sys.argv.index("-f") + 1
        if index_f < len(sys.argv):
            file_name = sys.argv[index_f]

    if not file_name:
        print("Error: File name is required when using -f flag")
        sys.exit(1)

    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

        if file_name:
            if not isinstance(path, str):
                raise ValueError(f"Invalid path: {path}")
            if not isinstance(file_name, str):
                raise ValueError(f"Invalid file_name: {file_name}")

            file_path = os.path.join(path, file_name)
    else:
        if not file_name:
            raise ValueError("File name must be specified")
        file_path = file_name

    line_count = 1
    if os.path.exists(file_path):
        with open(file_path, "r") as existing_file:
            lines = existing_file.readlines()
            if lines:
                line_count = len(lines) + 1

    with open(file_path, "a") as new_file:
        if line_count > 1:
            new_file.write("\n")

        time = datetime.now()
        new_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            info = input("Enter content line or 'stop': ")
            if info.lower() == "stop":
                break
            new_file.write(f"{line_count} {info}\n")
            line_count += 1


if __name__ == "__main__":
    main()
