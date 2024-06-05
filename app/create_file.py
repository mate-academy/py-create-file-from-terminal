import os
import datetime
from sys import argv


def create_file(path: str, filename: str, content: list[str]) -> None:
    full_path = os.path.join(path, filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(full_path)
    try:
        with open(full_path, "a") as f:
            if not file_exists:
                f.write(f"{timestamp}\n")
            else:
                f.write(f"\n{timestamp}\n")

            for i, line in enumerate(content, 1):
                f.write(f"{i} {line}\n")

        print(f"File created successfully: {full_path}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
    except PermissionError:
        print("Error: Permission denied to create file or directory.")


def get_content() -> list[str]:
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def main() -> None:
    if len(argv) < 3:
        print("Usage: python create_file.py [-d dir1 dir2] -f filename")
        return

    dir_path = ""
    filename = ""
    create_dir = False
    create_file_flag = False

    args = iter(argv[1:])
    for arg in args:
        if arg == "-d":
            create_dir = True
            dir_parts = []
            for dir_part in args:
                if dir_part.startswith("-"):
                    args = [dir_part] + list(args)
                    break
                dir_parts.append(dir_part)
            dir_path = os.path.join(*dir_parts)
        elif arg == "-f":
            create_file_flag = True
            filename = next(args, "")
        else:
            print(f"Invalid argument: {arg}")
            return

    if create_dir:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created successfully: {dir_path}")
        except PermissionError:
            print("Error: Permission denied to create directory.")
            return

    if not create_file_flag or not filename:
        print("Error: Filename not specified.")
        return

    content = get_content()
    create_file(dir_path, filename, content)


if __name__ == "__main__":
    main()
