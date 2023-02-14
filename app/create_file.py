import datetime
import os
import sys


def func(directory_path: list[str]) -> None:
    if "-f" in directory_path and "-d" in directory_path:
        path = directory_path[
            directory_path.index("-d") + 1: directory_path.index("-f")
        ]
        path = (
            making_directories(path) + "/"
            + directory_path[directory_path.index("-f") + 1]
        )
        making_file_and_content(path)
    elif "-f" in directory_path and "-d" not in directory_path:
        path = directory_path[directory_path.index("-f") + 1]
        making_file_and_content(path)
    elif "-d" in directory_path and "-f" not in directory_path:
        path = directory_path[directory_path.index("-d") + 1:]
        making_directories(path)


def making_directories(path: str) -> str:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)
    return path


def making_file_and_content(path: str) -> None:
    with open(path, "a") as file_name:
        file_name.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        line_counter = 0
        while True:
            text = input("Enter new line of content: ")
            line_counter += 1
            if text == "stop":
                break
            file_name.write(f"{line_counter} {text}" + "\n")
        file_name.write("\n")


if __name__ == "__main__":
    directory_path = sys.argv
    func(directory_path)
