import os
import sys
from datetime import datetime


def create_dir_and_file(
        path: list,
        file_name: str,
        value: list
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    line = [f"{i} {text}" for i, text in enumerate(value, start=1)]

    if path:
        destination = os.path.join(*path, file_name)
    else:
        destination = file_name

    if os.path.exists(destination):
        with open(destination, "a") as file:
            file.write("\n\n" + timestamp + "\n" + "\n".join(line))
    else:
        with open(destination, "w") as file:
            file.write(timestamp + "\n" + "\n".join(line))


def create_data_for_file() -> None:
    path = []
    file_name = ""
    value = []

    for_index = 0
    while for_index < len(sys.argv[1:]):
        element = sys.argv[1:][for_index]
        if element == "-d":
            path = sys.argv[1:][for_index + 1:]
            break
        elif element == "-f":
            file_name = sys.argv[1:][for_index + 1]
            break
        else:
            for_index += 1

    if path:
        os.makedirs(os.path.join(*path), exist_ok=True)

    if file_name:
        while True:
            new_line = input("Enter your message: ")
            if new_line == "stop":
                break
            value.append(new_line)

        create_dir_and_file(path, file_name, value)


if __name__ == "__main__":
    create_data_for_file()
