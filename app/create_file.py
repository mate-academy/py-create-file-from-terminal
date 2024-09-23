import os
import datetime

from sys import argv


def create_file(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, "a") as source_file:
            source_file.write("\n")
    with open(file_name, "a") as source_file:
        time_output = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{time_output}\n")
        page_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                break
            source_file.write(f"{page_number} {line_content}\n")
            page_number += 1


def main() -> None:
    char_f = "-f"
    char_d = "-d"
    if (char_f in argv and char_d in argv
            and argv.index(char_f) > argv.index(char_d)):
        directory_names = os.path.join(*argv[2:argv.index(char_f):])
        file_name = os.path.join(*argv[argv.index(char_f) + 1::])
        if os.path.isdir(directory_names):
            os.chdir(directory_names)
            create_file(file_name)

        else:
            os.makedirs(directory_names)
            os.chdir(directory_names)
            create_file(file_name)

    elif (char_f in argv and char_d in argv
          and argv.index(char_f) < argv.index(char_d)):
        directory_names = os.path.join(*argv[argv.index(char_d) + 1::])
        file_name = os.path.join(*argv[2:argv.index(char_d):])
        if os.path.isdir(directory_names):
            os.chdir(directory_names)
            create_file(file_name)

        else:
            os.makedirs(directory_names)
            os.chdir(directory_names)
            create_file(file_name)

    elif char_f in argv:
        file_name = argv[-1]
        create_file(file_name)

    elif char_d in argv:
        directory_names = os.path.join(*argv[2::])
        if not os.path.isdir(directory_names):
            os.makedirs(directory_names)


main()
