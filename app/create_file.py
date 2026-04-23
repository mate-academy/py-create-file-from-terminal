import os
import datetime
import argparse


def write_content_to_file(path: str) -> None:
    with open(path, "a+") as file:
        lines = []
        num_line = 1
        while True:

            new_line = input("Enter content line: ")
            if new_line == "stop":
                lines.append("\n")
                break
            lines.append(f"{str(num_line)} {new_line}\n")
            num_line += 1

        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

        file.write(date_str)
        file.writelines(lines)


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories", nargs="*", type=str, default=[])
    parser.add_argument("-f", "--file_name", type=str)

    args = parser.parse_args()

    file_name = args.file_name
    dir_path = os.path.join(*args.directories)

    os.makedirs(dir_path, exist_ok=True)

    if file_name:
        write_content_to_file(os.path.join(dir_path, file_name))


create_file()
