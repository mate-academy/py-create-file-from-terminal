import os.path
import sys
from datetime import datetime


def create_file() -> None:
    dirs_name = None
    file_name = None

    text_from_terminal = sys.argv

    if "-f" in text_from_terminal:
        file_name = text_from_terminal[-1]
        text_from_terminal = text_from_terminal[:-2]

    if "-d" in text_from_terminal:
        dirs_name = os.path.join(*text_from_terminal[2:])

    if dirs_name:
        if not os.path.isdir(os.path.join(os.getcwd(), dirs_name)):
            os.makedirs(os.path.join(os.getcwd(), dirs_name))

        os.chdir(os.path.join(os.getcwd(), dirs_name))

    if file_name:
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


if __name__ == "__main__":
    create_file()
