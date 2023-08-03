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


def create_directories_and_file(
        directories_to_create: list,
        file_to_create: str
) -> None:
    create_only_directories(os.path.join(*directories_to_create))
    file_path = os.path.join(*directories, file_to_create)
    create_only_file(file_path)


if __name__ == "__main__":
    if sys.argv[1] == "-d" and sys.argv[-2] == "-f":
        directories = sys.argv[2:-2]
        file_name = sys.argv[-1]
        create_directories_and_file(directories, file_name)
    elif sys.argv[1] == "-f" and sys.argv[3] == "-d":
        directories = sys.argv[4:]
        file_name = sys.argv[2]
        create_directories_and_file(directories, file_name)
    elif sys.argv[1] == "-d":
        directories = sys.argv[2:]
        create_only_directories(os.path.join(*directories))
    else:
        create_only_file(sys.argv[2])
