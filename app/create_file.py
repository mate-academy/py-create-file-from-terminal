import datetime
import os
import sys


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_name = "/".join(
            sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        )
        file_name = sys.argv[sys.argv.index("-f") + 1]
        path = f"{os.getcwd()}/{dir_name}/{file_name}"
        os.makedirs(dir_name, exist_ok=True)

        with open(path, "a") as file:
            file.write(
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            counter = 1
            while True:
                content_line = input("Enter content line: ")
                if content_line == "stop":
                    break
                file.write(f"{counter} {content_line}\n")
                counter += 1
