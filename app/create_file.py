import sys
import os
import datetime


total_number_of_flags = len(sys.argv)
path = os.getcwd()
for flag_number in range(1, total_number_of_flags):
    if sys.argv[flag_number] == "-d":
        for flag_number_to_create_directory in range(
                flag_number + 1,
                total_number_of_flags
        ):
            if sys.argv[flag_number_to_create_directory] == "-f":
                break
            path = os.path.join(
                path,
                sys.argv[flag_number_to_create_directory]
            )
        os.makedirs(path)
    if sys.argv[flag_number] == "-f":
        with open(os.path.join(path, sys.argv[flag_number + 1]), "a") as file:
            current_date = datetime.datetime.now()
            file.write(str(current_date.strftime("%Y-%m-%d %X") + "\n"))
            content_line = ""
            while True:
                sys.stdout.write("Enter content line: ")
                content_line = input()
                if content_line == "stop":
                    break
                file.writelines(str(content_line + "\n"))
