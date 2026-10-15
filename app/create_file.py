import sys
import os
import datetime


def define_path() -> dict:
    current_flag = ""
    file_name = ""
    directories_list = []

    for arg in sys.argv[1:]:
        if arg == "-f":
            current_flag = "-f"
            continue
        elif arg == "-d":
            current_flag = "-d"
            continue

        if current_flag == "-f":
            file_name = arg
        else:
            directories_list.append(arg)
    directories = os.path.join(*directories_list) if directories_list else ""
    return (directories, file_name)


def create_file() -> None:
    directories, file_name = define_path()
    if directories:
        os.makedirs(directories, exist_ok=True)

    if file_name:
        file_path_base = os.path.join(directories, file_name)
        file_path = os.path.normpath(file_path_base)
        mode = "w"
        if os.path.isfile(file_path):
            mode = "a"

        with open(file_path, mode) as file:
            if mode == "a":
                file.write("\n\n")
            file.write(
                f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            )
            line_counter = 1
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                file.write(f"\n{line_counter} {input_text}")
                line_counter += 1


create_file()
