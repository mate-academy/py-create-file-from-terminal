import sys
import os
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    directories = []
    file_name = None

    index = 0
    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1
            while (
                    index < len(arguments)
                    and not arguments[index].startswith("-")
            ):
                directories.append(arguments[index])
                index += 1
            continue

        if arguments[index] == "-f":
            index += 1
            if index < len(arguments):
                file_name = arguments[index]
            index += 1
            continue

        index += 1

    return directories, file_name


def create_directory_path(directories: list) -> str:
    if not directories:
        return ""
    return os.path.join(*directories)


def create_directories(path: str) -> None:
    if path:
        os.makedirs(path, exist_ok=True)


def read_user_content() -> list:
    content_lines = []
    line_number = 1

    while True:
        user_input = input("Enter content line: ")

        if user_input.lower() == "stop":
            break

        content_lines.append(f"{line_number} {user_input}")
        line_number += 1

    return content_lines


def build_content_block(lines: list) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = f"{timestamp}\n"
    block += "\n".join(lines)
    block += "\n"

    return block


def write_to_file(file_path: str, content_block: str) -> None:
    file_exists = os.path.exists(file_path)

    mode = "a" if file_exists else "w"

    with open(
            file_path,
            mode,
            encoding="utf-8",
    ) as file:
        if file_exists:
            file.write("\n" + content_block)
        else:
            file.write(content_block)


def main() -> None:
    arguments = sys.argv[1:]
    directories, file_name = parse_arguments(arguments)

    if not file_name:
        print(
            "Ошибка: необходимо указать имя файла с помощью флага -f"
        )
        return

    directory_path = create_directory_path(directories)
    create_directories(directory_path)

    file_path = os.path.join(directory_path, file_name)

    print(f"Enter {file_name}")
    content_lines = read_user_content()

    content_block = build_content_block(content_lines)
    write_to_file(file_path, content_block)

    print(f"Файл успешно создан или обновлён: {file_path}")


if __name__ == "__main__":
    main()
