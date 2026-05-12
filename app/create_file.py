import sys
import datetime
import os


def create_file(path_before_file: str) -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    full_path = os.path.join(path_before_file, file_name)
    blank_line = "\n" if os.path.exists(full_path) else ""
    with open(full_path, "a") as f:
        f.write(f"{blank_line}"
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        number_line = 1
        while True:
            file_content = input("Enter content line: ")
            if file_content == "stop":
                break
            f.write(f"{number_line} {file_content}\n")
            number_line += 1


directory_path = "."

if "-d" in sys.argv:
    parts = []
    for part in sys.argv[sys.argv.index("-d") + 1:]:
        if part.startswith("-"):
            break
        parts.append(part)

    if parts:
        directory_path = os.path.join(*parts)
        os.makedirs(directory_path, exist_ok=True)

if "-f" in sys.argv:
    create_file(directory_path)
