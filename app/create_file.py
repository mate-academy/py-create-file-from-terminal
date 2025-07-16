import datetime
import os
import sys


if "-d" in sys.argv and "-f" in sys.argv:
    path = sys.argv[3:sys.argv.index("-f")]
    os.makedirs(os.path.join(*path))
    with open(os.path.join(*path, sys.argv[-1]), "a") as my_file:
        my_file.write(
            os.path.join(*path, sys.argv[-1]) + "\n"
            + f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        )
        line_number = 1
        while True:
            content = input("Enter content line:")
            if content == "stop":
                break
            my_file.write(f"{line_number} {content}\n")
            line_number += 1
elif sys.argv[2] == "-d":
    path = sys.argv[3:]
    os.makedirs(os.path.join(*path))
else:
    with open(sys.argv[3], "a") as my_file:
        my_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        line_number = 1
        while True:
            content = input("Enter content line:")
            if content == "stop":
                break
            my_file.write(f"{line_number} {content}\n")
            line_number += 1
