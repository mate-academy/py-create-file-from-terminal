import os
import sys
import datetime


def create_file() -> None:
    arguments = sys.argv[1:]

    if "-d" in arguments and "-f" in arguments:
        directory_flag_index = arguments.index("-d")
        file_flag_index = arguments.index("-f")

        file_name = arguments[file_flag_index + 1]
        if directory_flag_index < file_flag_index:
            directories = arguments[directory_flag_index + 1:file_flag_index]
        else:
            directories = arguments[directory_flag_index + 1:]

        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "a", encoding="utf-8") as file:
            if os.path.getsize(file_path) > 0:
                file.write("\n")

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + "\n")

            mark = 1
            line_input = input("Enter content line: ")
            while line_input != "stop":
                file.write(f"{mark} {line_input}\n")
                mark += 1
                line_input = input("Enter content line: ")

    elif "-d" in arguments:
        directories = arguments[arguments.index("-d") + 1:]
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    elif "-f" in arguments:
        file_name = arguments[arguments.index("-f") + 1]
        with open(file_name, "a", encoding="utf-8") as file:
            if os.path.getsize(file_name) > 0:
                file.write("\n")

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
            file.write(timestamp + "\n")

            mark = 1
            line_input = input("Enter content line: ")
            while line_input != "stop":
                file.write(f"{mark} {line_input}\n")
                mark += 1
                line_input = input("Enter content line: ")


create_file()
