from os import path
import sys
from os import makedirs
from datetime import datetime


arguments = sys.argv
directories = []
path_to_file = ""
for index in range(len(arguments)):
    if arguments[index] == "-d":
        for argument in arguments[index + 1:]:
            if argument == "-f":
                break
            directories.append(argument)
        path_to_file = path.join(*directories)
        makedirs(path_to_file, exist_ok=True)
    if arguments[index] == "-f":
        with open(
                path.join(*directories, arguments[index + 1])
                , "w") as output_file:
            current_date_mark = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            output_file.write(
                f"{current_date_mark}\n")
            while True:
                input_value = input("Enter content line:")
                if input_value == "exit":
                    break
                output_file.write(f"{input_value}\n")
