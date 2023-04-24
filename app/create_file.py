import sys
import os
import datetime


def create_file(argv: list) -> None:
    path_list = ""
    if "-d" in argv:
        if "-f" in argv:
            if argv.index("-d") > argv.index("-f"):
                path_list = argv[argv.index("-d") + 1:]
            else:
                path_list = argv[argv.index("-d") + 1: argv.index("-f")]
        else:
            path_list = argv[argv.index("-d") + 1:]
        os.makedirs(os.path.join(*path_list), exist_ok=True)

    if "-f" in argv:
        file_name = argv[argv.index("-f") + 1]
        path = os.path.join(*path_list, file_name)
        with open(path, "a") as file:
            file.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
            number_line = 1
            while True:
                line_text = input("Enter content line: ")
                if line_text == "stop":
                    file.write("\n")
                    break
                file.write(f"{number_line} {line_text}\n")
                number_line += 1


create_file(sys.argv)
