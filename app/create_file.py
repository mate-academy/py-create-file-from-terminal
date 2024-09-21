import os
import datetime

from sys import argv


def create_file(file_name: str) -> None:
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


def create_directory() -> None:
    if "-f" in argv and "-d" in argv and argv.index("-f") > argv.index("-d"):
        create_directory_names_list = os.path.join(*argv[2:argv.index("-f"):])
        create_file_name = os.path.join(*argv[argv.index("-f") + 1::])
        if os.path.isdir(create_directory_names_list):
            os.chdir(create_directory_names_list)
            create_file(create_file_name)

        else:
            os.makedirs(create_directory_names_list)
            os.chdir(create_directory_names_list)
            create_file(create_file_name)

    elif "-f" in argv and "-d" in argv and argv.index("-f") < argv.index("-d"):
        directory_names = os.path.join(*argv[argv.index("-d") + 1::])
        create_file_name = os.path.join(*argv[2:argv.index("-d"):])
        if os.path.isdir(directory_names):
            os.chdir(directory_names)
            create_file(create_file_name)

        else:
            os.makedirs(directory_names)
            os.chdir(directory_names)
            create_file(create_file_name)

    elif "-f" in argv:
        create_file(argv[-1])

    elif "-d" in argv:
        os.makedirs(os.path.join(*argv[2::]))


create_directory()
