import sys
import os
import datetime


def write_to_file(path_file: str) -> None:
    with open(path_file, "a") as file:
        now = datetime.datetime.now()
        file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")}\n")
        line_count = 0

        while True:
            new_line = input("Enter content line: ")

            if new_line == "stop":
                break

            line_count += 1
            file.write(f"{line_count} {new_line}\n")


if sys.argv[1] == "-f":
    write_to_file(sys.argv[2])

elif sys.argv[1] == "-d":

    if "-f" not in sys.argv[2:]:
        os.makedirs("/".join(sys.argv[2:]), exist_ok=True)

    else:
        os.makedirs("/".join(sys.argv[2:-2]), exist_ok=True)
        index = sys.argv.index("-f")
        file_path = f"{"/".join(sys.argv[2:-2])}/{sys.argv[index + 1]}"
        write_to_file(file_path)
