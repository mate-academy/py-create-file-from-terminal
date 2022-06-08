import os
import sys
from datetime import datetime

arguments = sys.argv
dir_path = os.getcwd()

for i in range(1, len(arguments)):

    if arguments[i - 1] == "-d":
        dir_path = os.path.join(os.getcwd(), arguments[i])
        os.mkdir(dir_path)

        for j in range(i + 1, len(arguments)):

            if arguments[j] == "-f":
                file = open(os.path.join(dir_path, arguments[j + 1]), "w")
                file.close()
                break

            dir_path = os.path.join(dir_path, arguments[j])
            os.mkdir(dir_path)

    elif arguments[i - 1] == "-f":
        line_number = 1

        if os.path.exists(arguments[i]):
            with open(arguments[i], "a") as file:
                date_on_page = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.writelines(f"{date_on_page}\n")
                line_content = input("Enter content line: ")

                while line_content != "stop":
                    file.writelines(f"{line_number} {line_content}\n")
                    line_number += 1
                    line_content = input("Enter content line: ")
                file.writelines("\n")
        else:
            with open(os.path.join(dir_path, arguments[i]), "w") as file:
                date_on_page = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.writelines(f"{date_on_page}\n")
                line_content = input("Enter content line: ")

                while line_content != "stop":
                    file.writelines(f"{line_number} {line_content}\n")
                    line_number += 1
                    line_content = input("Enter content line: ")
                file.writelines("\n")
