import os.path
import sys
from datetime import datetime


def create_directory(dirs_name: str) -> None:
    if not os.path.isdir(os.path.join(os.getcwd(), dirs_name)):
        os.makedirs(os.path.join(os.getcwd(), dirs_name))

    os.chdir(os.path.join(os.getcwd(), dirs_name))


def create_or_update_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S") + "\n")
        line_number = 1

        while True:
            text = input("Enter content line: ")

            if text == "stop":
                break
            file.write(f"{line_number} {text}\n")
            line_number += 1

        file.write("\n")


def main() -> None:
    text_from_terminal = sys.argv

    if "-d" in text_from_terminal:
        d_index = text_from_terminal.index("-d")
        dirs_name = text_from_terminal[d_index + 1:]

        if "-f" in dirs_name:
            dirs_name = dirs_name[:dirs_name.index("-f")]
        dirs_name = os.path.join(*dirs_name)

        create_directory(dirs_name=dirs_name)

    if "-f" in text_from_terminal:
        f_index = text_from_terminal.index("-f")
        file_name = text_from_terminal[f_index + 1]
        create_or_update_file(file_name=file_name)


if __name__ == "__main__":
    main()
