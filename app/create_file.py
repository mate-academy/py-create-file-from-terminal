import os
import sys
import datetime
from typing import Any


def create_a_directory(dir_path: str | bytes) -> Any:
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_a_file(file_name: str) -> Any:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = []

    while True:
        input_content = input("Enter content line: ")
        if input_content.upper() == "STOP":
            break
        text.append(input_content)

    with open(file_name, "a") as file:
        file.write(f"\n{timestamp}\n")
        for index, content in enumerate(text, start=1):
            file.write(f"{index} {content}\n")


def main() -> None:
    data = sys.argv[1:]
    print(sys.argv)

    if "-d" in data and "-f" in data:
        d_index = data.index("-d")
        f_index = data.index("-f")
        if d_index < f_index:
            directory = create_a_directory(
                os.path.join(*data[d_index + 1:f_index])
            )
            path = os.path.join(directory, data[f_index + 1])
        else:
            directory = create_a_directory(os.path.join(*data[d_index + 1:]))
            path = os.path.join(directory, data[f_index + 1])
        create_a_file(path)
    elif "-d" in data:
        create_a_directory(os.path.join(*data[data.index("-d") + 1:]))
    elif "-f" in data:
        create_a_file(data[data.index("-f") + 1])


if __name__ == "__main__":
    main()
