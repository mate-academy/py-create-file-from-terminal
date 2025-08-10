import datetime
import os
import sys


def create_file(given: list) -> None:
    if "-d" in given and "-f" not in given:
        os.makedirs("app/dir1/dir2")

    def write_text_to_file() -> None:
        current = datetime.datetime.now()
        f.write(f"{current.strftime('%Y-%m-%d %X')}\n")
        line = 1
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                f.write("\n")
                break
            f.write(f"{line} {text}\n")
            line += 1

    if "-d" not in given and "-f" in given:
        with open("app/file.txt", "a") as f:
            write_text_to_file()

    if "-d" in given and "-f" in given:
        with open("app/dir1/dir2/file.txt", "a") as f:
            write_text_to_file()


create_file(sys.argv)
