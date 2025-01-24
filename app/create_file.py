import os
import sys
import datetime


def create_file(file_name: str) -> None:

    is_new_file = os.path.exists("file_name")

    with open(file_name, "a") as source_file:

        if not is_new_file:
            source_file.write("\n")

        line_count = 0
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        while True:
            input_line = input("Enter content line:")

            if input_line == "stop":
                break

            line_count += 1
            source_file.write(f"{line_count} {input_line}")


def create_directory(path: str | bytes) -> None:

    if not os.path.exists(path):
        os.makedirs(path)

    os.chdir(path)


if __name__ == "__main__":
    command = sys.argv[1:]
    if command[0] == "-d":
        path = []
        for directory in command[1:]:
            if directory == "-f":
                break
            path.append(str(directory))
        create_directory(os.path.join(*path))
    if "-f" in command:
        create_file(command[-1])
