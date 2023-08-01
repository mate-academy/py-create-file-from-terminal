from sys import argv
import os
from datetime import datetime


if len(argv) > 2:

    parent_dir = "app"

    for i in range(len(argv)):

        if argv[i] == "-d":

            last_index_dir = argv.index("-f") if "-f" in argv else len(argv)

            for directory in argv[i + 1:last_index_dir]:
                parent_dir = os.path.join(parent_dir, directory)
            if not os.path.isdir(parent_dir):
                os.makedirs(parent_dir)

        if argv[i] == "-f":

            page_number = 1
            file_name = os.path.join(parent_dir, argv[i + 1])

            with open(file_name, "a") as source_file:
                if not os.stat(file_name).st_size == 0:
                    source_file.write("\n\n")
                source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                current_line = input("Enter content line:")
                while not current_line == "stop":
                    source_file.write(f"\n{page_number} {current_line}")
                    page_number += 1
                    current_line = input("Enter content line:")
