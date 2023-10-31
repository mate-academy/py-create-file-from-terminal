from datetime import datetime
import sys
import os


def create_path(directories: list) -> str:
    path = os.getcwd()
    for part in directories:
        path = os.path.join(path, part)
        if os.path.exists(path):
            continue
        os.makedirs(path)
    return path


def create_file(filename: str, path: str = "") -> None:
    file_path = os.path.join(path, filename)
    with open(file_path, "a") as file:
        file.write(create_content())


def create_content() -> str:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return "\n".join(content)


def main() -> None | str:
    input_data = sys.argv

    if "-d" in input_data and "-f" in input_data:
        dirs = input_data[input_data.index("-d") + 1: input_data.index("-f")]
        file_name = input_data[input_data.index("-f") + 1]
        return create_file(file_name, create_path(dirs))
    elif "-f" in input_data:
        file_name = input_data[input_data.index("-f") + 1]
        return create_file(file_name)
    elif "-d" in input_data:
        dirs = input_data[input_data.index("-d") + 1:]
        return create_path(dirs)


if __name__ == "__main__":
    main()
