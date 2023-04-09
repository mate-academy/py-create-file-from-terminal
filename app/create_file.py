import os
import sys
import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(*args) -> None:
    count = 1
    with open(os.path.join(*args), "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{count} {line}\n")
            count += 1


def total_creation() -> None:
    path_list = sys.argv

    if "-d" in path_list and "-f" in path_list:
        file_name = path_list[path_list.index("-f") + 1:]
        path_to_file = create_path(
            path_list[path_list.index("-d") + 1:path_list.index("-f")]
        )
        create_file(path_to_file, file_name)
    elif "-d" in path_list and "-f" not in path_list:
        path_to_file = path_list[path_list.index("-d") + 1:]
        create_path(path_to_file)
    elif "-d" not in path_list and "-f" in path_list:
        file_name = path_list[path_list.index("-f") + 1:]
        create_file(file_name)


if __name__ == "__main__":
    total_creation()
