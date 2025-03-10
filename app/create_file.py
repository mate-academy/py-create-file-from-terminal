import sys
import os
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    directory_parts = []
    file_name = None

    i = 1
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return directory_parts, file_name


def create_directory(directory_parts: list) -> str | None:
    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
        return directory_path
    return None


def get_file_content() -> list[str]:
    content = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    return content


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file_obj:
        file_obj.write(f"{timestamp}\n")
        for i, conten_line in enumerate(content, 1):
            file_obj.write(f"{i} {conten_line}\n")
        file_obj.write("\n")


def main() -> None:
    directory_parts, file_name = parse_arguments(sys.argv)
    directory_path = create_directory(directory_parts)

    if file_name:
        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name
        content = get_file_content()
        write_to_file(file_path, content)
        print(f"File created/updated at: {file_path}")
    else:
        print("No file name provided. "
              "Only directory was created if specified.")


if __name__ == "__main__":
    main()
