import sys
import os
import datetime


py_variables = sys.argv
file_dir = os.getcwd()


def make_dirs(this_dir: str, dir_list: list) -> str:
    final_path = os.path.join(this_dir, *dir_list)
    os.makedirs(final_path, exist_ok=True)
    return final_path


def make_file(this_dir: str, file_name: str) -> None:
    with open(os.path.join(this_dir, file_name), "a") as file:
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(stamp + "\n")
        index = 1
        while True:
            input_result = input("Enter content line: ")
            if input_result == "stop":
                break
            file.write(f"{index} " + input_result + "\n")
            index += 1


if "-d" in py_variables and "-f" in py_variables:
    dir_variables = py_variables[2:py_variables.index("-f")]
    file_variable = py_variables[-1]

    new_path = make_dirs(file_dir, dir_variables)
    make_file(new_path, file_variable)
elif "-d" in py_variables:
    file_dir = make_dirs(file_dir, py_variables[2:])
elif "-f" in py_variables:
    make_file(file_dir, py_variables[-1])
