import os
import sys
from datetime import datetime


print("Argument List:", sys.argv)
arguments = sys.argv[1:]

if "-f" in arguments:
    file_name = arguments[arguments.index("-f") + 1]

    if "-d" in arguments:
        file_path = os.path.join(
            *arguments[arguments.index("-d") + 1:arguments.index("-f")]
        )
        os.makedirs(file_path, exist_ok=True)
        file_name = os.path.join(file_path, file_name)

    with open(file_name, "w") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            new_file.write(content + "\n")

else:
    file_path = os.path.join(*arguments[2:])
    os.makedirs(file_path, exist_ok=True)
