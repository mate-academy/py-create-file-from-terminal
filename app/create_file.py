import sys
import os
from datetime import datetime


arguments = sys.argv

directory = []
file_name = None

if len(arguments) > 1:
    i = 1
    while i < len(arguments):
        if arguments[i] == "-d":
            i += 1
            while i < len(arguments) and not arguments[i].startswith("-"):
                directory.append(arguments[i])
                i += 1
        elif arguments[i] == "-f":
            i += 1
            if i < len(arguments):
                file_name = arguments[i]
                i += 1
        else:
            i += 1

if directory:
    for directory_name in directory:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        else:
            print(f"Directory '{directory_name}' already exists.")

if file_name:
    if directory:
        file_name = os.path.join(directory[-1], file_name)

    if os.path.exists(file_name):
        print(f"File '{file_name}' already exists.")
        mode = "a"
    else:
        print(f"File '{file_name}' created successfully.")
        mode = "w"

    with open(file_name, mode) as file:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f"Timestamp: {timestamp}\n")
        print(f"Created timestamp: {timestamp}")

        print("Enter the text to write to the file. Type 'stop' to finish.")
        line_number = 1
        while True:
            user_input = input(f"Enter content line: {line_number} ")
            if user_input.lower() == "stop":
                break
            file.write(f"{user_input}\n")
            line_number += 1

    print(f"File {file_name} created successfully.")
else:
    print("File name not specified.")
print("Done.")
