import os
import sys
from datetime import datetime
from typing import List


def main(term_args: List[str]) -> None:

    if ("-d" in term_args) and ("-f" in term_args):

        file_name = term_args[-1]
        index_f = term_args.index("-f")
        path = term_args[2:index_f]
        directory = os.path.join(*path)

        create_dir(directory=directory)
        write_to_file(directory=directory, file_name=file_name)

    elif "-d" in term_args:

        path = term_args[2:]
        directory = os.path.join(*path)
        create_dir(directory=directory)

    else:
        file_name = term_args[-1]
        write_to_file(directory="", file_name=file_name)


def create_dir(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def write_to_file(directory: str, file_name: str) -> None:
    with open(f"{os.path.join(directory, file_name)}", "a") as file_record:
        file_record.write(
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        number_line = 1

        while True:
            record_info = input("Enter content line: ")
            if record_info.lower() == "stop":
                file_record.write("\n\n")
                break
            file_record.write(
                f"\n{number_line} {record_info}"
            )
            number_line += 1


if __name__ == "__main__":
    main(sys.argv)
