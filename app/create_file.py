import os
import sys
from datetime import datetime


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_count = 1

    with open(file_name, "a" if os.path.exists(file_name) else "w") as f:
        if f.tell() != 0:
            f.write("\n\n")
        f.write(timestamp)
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"\n{line_count} {line}")
            line_count += 1


def command_check() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: python create_file.py -d <directory_path> -f <file_name>"
        )
        sys.exit(1)


def flags_check() -> None:
    if sys.argv.__contains__("-d") and sys.argv.__contains__("-f"):
        directory_path = sys.argv[2:sys.argv.index("-f")]
        os.makedirs(os.path.join(*directory_path), exist_ok=True)
        file_to_create = sys.argv[sys.argv.index("-f") + 1]
        os.chdir(os.path.join(*directory_path))
        create_file(file_to_create)
    elif sys.argv.__contains__("-d") and not sys.argv.__contains__("-f"):
        directory_path = sys.argv[2:]
        os.makedirs(os.path.join(*directory_path), exist_ok=True)
    elif not sys.argv.__contains__("-d") and sys.argv.__contains__("-f"):
        file_to_create = sys.argv[sys.argv.index("-f") + 1]
        create_file(file_to_create)
    elif not sys.argv.__contains__("-d") and not sys.argv.__contains__("-f"):
        print("Invalid flag. Use -d or -f.")
        sys.exit(1)


if __name__ == "__main__":
    command_check()
    flags_check()
