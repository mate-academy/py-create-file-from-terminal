import os
import sys
from datetime import datetime


def create_file(file_name: str):
    with open(file_name, "w") as file:
        date_on_page = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.writelines(f"{date_on_page}\n")
        line_number = 1
        line_content = input("Enter content line: ")

        while line_content != "stop":
            file.writelines(f"{line_number} {line_content}\n")
            line_number += 1
            line_content = input("Enter content line: ")
        file.writelines("\n")


def create_file_and_directories():
    arguments = sys.argv
    dir_path = os.getcwd()

    for i in range(1, len(arguments)):
        if arguments[i - 1] == "-d":
            dir_path = os.path.join(os.getcwd(), arguments[i])
            os.mkdir(dir_path)

            for j in range(i + 1, len(arguments)):

                if arguments[j] == "-f":
                    file_name = os.path.join(dir_path, arguments[j + 1])
                    create_file(file_name)
                    break

                dir_path = os.path.join(dir_path, arguments[j])
                os.mkdir(dir_path)
            break

        elif arguments[i - 1] == "-f":
            file_name = os.path.join(dir_path, arguments[i])
            create_file(file_name)
            break


create_file_and_directories()


