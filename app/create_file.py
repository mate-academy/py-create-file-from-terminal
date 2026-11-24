import datetime

import os

import sys


directory_path = ""
for word in range(len(sys.argv)):
    if sys.argv[word] == "-d":
        i = word + 1
        dir_parts = []
        while i < len(sys.argv) and sys.argv[i] != "-f":
            dir_parts.append(sys.argv[i])
            i += 1
        directory_path = os.path.join(*dir_parts)
        os.makedirs(directory_path, exist_ok=True)


for word in range(len(sys.argv)):
    if sys.argv[word] == "-f":
        i = word + 1
        filename = sys.argv[i]
        file_path = os.path.join(directory_path, filename)\
            if directory_path else filename
        if os.path.exists(file_path):
            with open(file_path, "a") as source_file:
                source_file.write("\n")
                source_file.write("\n")
        with open(file_path, "a") as source_file:
            current_date = datetime.datetime.now()
            source_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S"))
            line = input("Enter content line: ")
            num_of_line = 0
            while line != "stop":
                source_file.write("\n")
                num_of_line += 1
                source_file.write(f"{num_of_line} {line}")
                line = input("Enter content line: ")
