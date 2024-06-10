import os
import sys
from datetime import datetime


path = ""

if "-d" in sys.argv:
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)
    path = "/".join(sys.argv[sys.argv.index("-d") + 1:end_index])

    os.makedirs(path, exist_ok=True)

    path += "/"


if "-f" in sys.argv:
    path += sys.argv[-1]

    with open(path, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'\n{timestamp}\n')

        numerator = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{numerator} {line}\n")
            numerator += 1
