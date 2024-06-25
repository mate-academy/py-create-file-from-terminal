import os
import sys
import datetime


def create_file() -> None:

    directory_path = ""

    if "-d" in sys.argv:
        if "-f" in sys.argv:
            directory_path = sys.argv[sys.argv.index("-d")
                                      + 1:sys.argv.index("-f")]

        else:
            directory_path = sys.argv[sys.argv.index("-d") + 1:]
        os.makedirs(os.path.join(*directory_path), exist_ok=True)

    if "-f" in sys.argv:
        file_name = sys.argv[-1]
        file_exists = False

        if os.path.exists(os.path.join(*directory_path, file_name)):
            file_exists = True

        with open(os.path.join(*directory_path, file_name), "a") as file:
            if file_exists:
                file.write("\n\n")

            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            row_number = 1

            while True:
                entered_info = input("Enter content line: ")
                if entered_info == "stop":
                    break
                file.write(f"\n{row_number} {entered_info}")
                row_number += 1


if __name__ == "__main__":
    create_file()
