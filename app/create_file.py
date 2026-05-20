from sys import argv
from os import path, makedirs
from datetime import datetime


def main(all_information: list) -> None:
    if "-d" in all_information and "-f" not in all_information:
        crate_dir(path.join(*all_information[1:]))
    if "-f" in all_information and "-d" not in all_information:
        create_file(all_information[-1])
    if "-d" in all_information and "-f" in all_information:
        dir_path = "/".join(sorted(all_information)[2:-1]) + "/"
        crate_dir(dir_path)
        create_file(dir_path + all_information[-1])


def crate_dir(dir_path: str) -> None:
    if not path.exists(dir_path):
        makedirs(dir_path)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        count_line = 1
        file.write(f"\n{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}\n")
        while True:
            text = str(input("Enter content line: "))
            if text == "stop":
                break
            file.write(f"{count_line} {text}\n")
            count_line += 1


if __name__ == "__main__":
    main(argv[1:])
