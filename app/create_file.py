import sys
import os
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        if "-f" in args:
            f_index = args.index("-f")
            directory_parts = args[d_index:f_index]
        else:
            directory_parts = args[d_index:]

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    return directory_parts, file_name


def create_directory(directory_parts: list) -> str | None:
    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
        return directory_path


def get_file_content() -> list[str]:
    return [
        line for line in iter(
            lambda: input("Enter content line: "), "stop"
        )
    ]


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file_obj:
        file_obj.write(f"{timestamp}\n")
        for i, content_line in enumerate(content, 1):
            file_obj.write(f"{i} {content_line}\n")
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
