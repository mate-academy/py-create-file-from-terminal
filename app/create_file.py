import os
import sys
import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file:
        file.write(content)


def get_input_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == 'stop':
            break
        lines.append(line)
    return lines


def main() -> None:
    args = sys.argv[1:]
    create_directory_flag = False
    create_file_flag = False
    parts_of_creating = []
    file_name = None

    for arg in args:
        if arg == '-d':
            create_directory_flag = True
        elif arg == '-f':
            create_file_flag = True
        elif create_directory_flag:
            parts_of_creating.append(arg)
        elif create_file_flag:
            file_name = arg

    if create_directory_flag:
        directory_path = os.path.join(*parts_of_creating)
        create_directory(directory_path)

    if create_file_flag:
        file_path = os.path.join(*parts_of_creating, file_name)
        content_lines = get_input_content()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content_lines = "\n".join(
            [f"{i+1} {line}" for i, line in
             enumerate(content_lines)]
        )
        content = f"{timestamp}\n{content_lines}"
        create_file(file_path, content)


if __name__ == '__main__':
    main()
