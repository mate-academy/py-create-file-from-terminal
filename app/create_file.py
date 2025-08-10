import sys
import os
from datetime import datetime


def create_file() -> None:
    try:
        user_input = sys.argv

        if "-d" in user_input:
            key_dir_index = user_input.index("-d")

            path_end = 0

            if "-f" in user_input:
                path_end = user_input.index("-f")
            else:
                path_end = len(user_input)

            path_way = "/".join(user_input[key_dir_index + 1 : path_end])

            os.makedirs(path_way, exist_ok=True)
            os.chdir(path_way)

        if "-f" in user_input:
            key_file_index = user_input.index("-f")
            file_name = user_input[key_file_index + 1]

            with open(file_name, "a+") as file:
                if file.tell() > 0:
                    file.write("\n")

                file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S" + "\n"))

                asking_user = True

                while asking_user:
                    new_line = input("Enter content line: ")

                    if new_line == "stop":
                        asking_user = False
                        break

                    file.write(new_line + "\n")
    except ValueError:
        return "Incorrect value"


if __name__ == "__main__":
    create_file()
