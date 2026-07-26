import datetime
import os
import sys


def create_only_directories(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def create_only_file(file_to_create: str) -> None:
    with open(file_to_create, "a") as new_file:
        page = 1
        new_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                new_file.write("\n")
                break
            new_file.write(f"{page} {new_line} \n")
            page += 1


def create_directories_and_file() -> None:
    file_index = sys.argv.index("-f") + 1
    directories_index = sys.argv.index("-d") + 1
    file_name = sys.argv[file_index]

    if file_index < directories_index:
        directories_to_create = (sys.argv[directories_index:
                                 max(file_index - 1, len(sys.argv))])
    else:
        directories_to_create = sys.argv[directories_index: file_index - 1]

    create_only_directories(os.path.join(*directories_to_create))
    file_path = os.path.join(*directories_to_create, file_name)
    create_only_file(file_path)


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        create_directories_and_file()
    elif "-d" in sys.argv and "-f" not in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:]
        create_only_directories(os.path.join(*directories))
    else:
        create_only_file(sys.argv[sys.argv.index("-f") + 1])
