from datetime import datetime
import os
import argparse


def main() -> None:
    dict_data = read_data()

    create_directories(dict_data["directories"])
    create_file(dict_data["directories"], dict_data["file"])


def create_directories(file_directory: str) -> None:
    os.makedirs(file_directory, exist_ok=True)


def create_file(file_directory: str, file_name: str) -> None:
    if not file_name:
        return

    with open(os.path.join(file_directory, file_name), "a") as file:
        file.writelines(
            datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n"
        )
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.writelines(new_line + "\n")


def read_data() -> dict:
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", type=str)
    parser.add_argument(
        "-d", "--directories",
        nargs="+",
        default=["".join(os.getcwd())]
    )

    args = parser.parse_args()

    arguments_dict = {
        "file": args.file,
        "directories": os.path.join(*args.directories)
    }

    return arguments_dict


if __name__ == "__main__":
    main()
