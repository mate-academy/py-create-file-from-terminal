import sys
import os
from datetime import datetime


def parse_arguments() -> tuple:
    args = iter(sys.argv[1:])
    directory_path, file_name = [], None

    for arg in args:
        if arg == "-d":
            directory_path = list(iter(lambda: next(args, "").strip("-"), ""))
        elif arg == "-f":
            file_name = next(args, None)
            if file_name is None or file_name.startswith("-"):
                print("Помилка: -f потребує ім'я файлу")
                sys.exit(1)

    return directory_path, file_name


def create_and_fill_file(directory_path: list, file_name: str) -> str:
    print("Введіть вміст файлу. Напишіть 'stop' для завершення:")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]

    for line_number, line in enumerate(iter(lambda: input("Enter content line: ").strip(), "stop"), 1):  # noqa E501
        content.append(f"{line_number} {line}")

    dir_path = os.path.join(*directory_path) if directory_path else ""
    if directory_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, file_name)
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write("\n".join(content) + "\n")

    return dir_path


def main() -> None:
    directory_path, file_name = parse_arguments()
    if file_name:
        create_and_fill_file(directory_path, file_name)


if __name__ == "__main__":
    main()
