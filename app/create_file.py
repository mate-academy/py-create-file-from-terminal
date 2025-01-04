import sys
from datetime import datetime
import os


current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

file_name_directory = sys.argv[2:]
file_name_directory = "/".join(file_name_directory)


if "-d" in sys.argv:
    os.makedirs(file_name_directory)

if "f" in sys.argv:
    with open(sys.argv[2], "a") as file:
        file.write(f"{formatted_time}\n")

        while True:
            file_input = input("Enter content line: ")
            if file_input == "stop":
                break
            file.write(f"{file_input}\n")
