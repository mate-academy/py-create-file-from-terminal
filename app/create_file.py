import sys
import os
import datetime


def create_path(directories: list) -> None:
    os.makedirs(os.path.join(*directories), exist_ok=True)


def write_to_file(file_path_and_name: str) -> None:
    page_number = 1

    with open(file_path_and_name, "a") as source_file:
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        )

        while True:
            input_line = input("Enter content line: ")
            if input_line.lower() == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{page_number} {input_line}\n")
            page_number += 1


def main() -> None:
    directories = []
    file_name = []

    base = sys.argv

    if "-f" in base and "-d" in base:
        if base.index("-d") < base.index("-f"):
            directories = base[base.index("-d") + 1:base.index("-f")]
            file_name = base[base.index("-f") + 1]
        else:
            file_name = base[base.index("-f") + 1]
            directories = base[base.index("-d") + 1:]
    elif "-d" in base and "-f" not in base:
        directories = base[base.index("-d") + 1:]
    elif "-d" not in base and "-f" in base:
        file_name = base[base.index("-f") + 1]

    if len(directories) != 0:
        create_path(directories)
    if len(file_name) != 0:
        write_to_file(os.path.join(*directories + file_name))


if __name__ == "__main__":
    main()
