from datetime import datetime
import os
import sys


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_to_file(file_path: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "w") as file:
        file.write(f"{timestamp}\n")
        file.writelines([f"{i + 1} {line}\n"
                         for i, line in enumerate(content_lines)])


def make_content() -> list:
    content_lines = []

    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        content_lines.append(content)
    return content_lines


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d") + 1
        file_index = args.index("-f") + 1

        if dir_index < file_index:
            directory_path = os.path.join(*args[dir_index:file_index - 1])
            file_name = args[file_index]

        else:
            directory_path = os.path.join(*args[dir_index:])
            file_name = args[file_index]

        create_directory(directory_path)
        file_path = os.path.join(directory_path, file_name)

        content = make_content()

        write_to_file(file_path, content)

    elif "-d" in args:
        dir_index = args.index("-d") + 1

        directory_path = os.path.join(*args[dir_index:])
        create_directory(directory_path)

    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_path = args[file_index]

        content = make_content()

        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
