import sys
from datetime import datetime
import os


def create_file() -> None:
    params = sys.argv
    if "-f" in params and "-d" in params:
        path = sys.argv[sys.argv.index("-d") + 1 : sys.argv.index("-f")]
        path.append(sys.argv[-1])
        path, og_path = os.path.join(*path), path
        if os.path.exists(path):
            with open(path, "a") as file_obj:
                file_obj.write("\n")
                write_to_file(file_obj)
        else:
            os.makedirs(os.path.join(*og_path[:-1]), exist_ok=True)
            with open(path, "a") as file_obj:
                write_to_file(file_obj)
    elif "-f" in params and os.path.exists(sys.argv[-1]):
        with open(sys.argv[-1], "a") as file_obj:
            file_obj.write("\n")
            write_to_file(file_obj)
    elif "-f" in params:
        with open(sys.argv[-1], "a") as file_obj:
            write_to_file(file_obj)


def write_to_file(file_obj: object) -> None:
    file_obj.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    counter = 1
    user_input = ""
    while user_input.strip().lower() != "stop":
        user_input = input("Enter content line: ")
        if user_input.strip().lower() != "stop":
            file_obj.write(f"{counter} {user_input}\n")
            counter += 1
