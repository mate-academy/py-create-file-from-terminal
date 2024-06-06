import os
import datetime
from sys import argv


def create_file(path: str, filename: str, content: list[str]) -> None:
    full_path = os.path.join(path, filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(full_path)
    try:
        with open(full_path, "a") as f:
            f.write(f"\n{timestamp}\n" if file_exists else f"{timestamp}\n")

            content_with_numbers = [f"{i + 1} {line}"
                                    for i, line in enumerate(content)]
            f.write("\n".join(content_with_numbers) + "\n")

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


def parse_arguments(args: list[str]) -> tuple[str, str]:
    dir_path = ""
    filename = ""
    create_dir = False
    create_file_flag = False
    i = 1

    while i < len(args):
        if args[i] == "-d":
            create_dir = True
            i += 1
            dir_parts = []
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            dir_path = os.path.join(*dir_parts)
        elif args[i] == "-f":
            create_file_flag = True
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: Filename not specified.")
                return "", ""
        else:
            print(f"Invalid argument: {args[i]}")
            return "", ""

    if create_dir:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created successfully: {dir_path}")
        except PermissionError:
            print("Error: Permission denied to create directory.")
            return "", ""

    if not create_file_flag or not filename:
        print("Error: Filename not specified.")
        return "", ""

    return dir_path, filename


def main() -> None:
    if len(argv) < 3:
        print("Python create_file.py [-d dir1 dir2] -f filename")
        return

    dir_path, filename = parse_arguments(argv)

    content = get_content()
    create_file(dir_path, filename, content)


if __name__ == "__main__":
    main()
