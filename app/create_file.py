from sys import argv
from os import makedirs, path
from datetime import datetime


args = argv

if "-d" in args:
    d_index = args.index("-d")
    given_path = argv[(d_index + 1) :]

    if "-f" in args:
        f_index = args.index("-f")
        given_path = args[(d_index + 1) : f_index]

    final_path = path.join(*given_path)

    makedirs(final_path, exist_ok=True)


if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]
    final_path = path.join(*given_path, file_name)

    if path.exists(final_path):
        file_exist = True

    with open(f"{final_path}", "a") as file:
        if file_exist is True:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(str(timestamp) + "\n")

        page_number = 1
        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{page_number} {line}" + "\n")
            page_number += 1
