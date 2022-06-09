import sys
import os
from datetime import datetime

if sys.argv[1] == "-d" and sys.argv[-2] != "-f":
    directories = ""

    for i in range(2, len(sys.argv)):
        directories += f"{sys.argv[i]}/"
        os.mkdir(directories)


if "-f" in sys.argv:

    time_now = datetime.now()
    time = time_now.strftime("%Y-%m-%d %H:%M:%S")

    if sys.argv[1] == "-f":
        file_name = sys.argv[2]
    else:
        file_name = sys.argv[-1]

    with open(file_name, 'a') as file_in:

        number_line = 1
        file_in.write(f"{time}\n")

        while True:
            lines = input("Enter content line: ")

            if lines == "stop":
                file_in.write("\n")
                break

            file_in.write(f"{number_line} {lines}\n")
            number_line += 1
