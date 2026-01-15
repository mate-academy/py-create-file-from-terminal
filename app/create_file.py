import sys
import os
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directory_parts: list[str] = []
    file_name: str | None = None

    if "-d" in arguments:
        directory_index = arguments.index("-d") + 1
        while (directory_index < len(arguments)
               and arguments[directory_index] not in ("-f",)):
            directory_parts.append(arguments[directory_index])
            directory_index += 1

    if "-f" in arguments:
        file_index = arguments.index("-f") + 1
        if file_index < len(arguments):
            file_name = arguments[file_index]

    return directory_parts, file_name


def get_content_lines() -> list[str]:
    content_lines: list[str] = []

    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        content_lines.append(user_input)

    return content_lines


def format_content(content_lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]

    for line_number, content_line in enumerate(content_lines, start=1):
        formatted_lines.append(f"{line_number} {content_line}")

    return "\n".join(formatted_lines) + "\n"


def create_directories(directory_parts: list[str]) -> str:
    directory_path = os.path.join(os.getcwd(), *directory_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def write_to_file(file_path: str, formatted_content: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(formatted_content)


def main() -> None:
    arguments = sys.argv[1:]

    directory_parts, file_name = parse_arguments(arguments)

    if not directory_parts and not file_name:
        print("Error: you must use -d, -f, or both.")
        return

    content_lines = get_content_lines()
    formatted_content = format_content(content_lines)

    base_path = os.getcwd()

    if directory_parts:
        base_path = create_directories(directory_parts)

    if file_name:
        file_path = os.path.join(base_path, file_name)
        write_to_file(file_path, formatted_content)
        print(f"File created or updated: {file_path}")


if __name__ == "__main__":
    main()
