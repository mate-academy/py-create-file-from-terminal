import sys
import os
import datetime


def create_directories() -> str:
    index_of_d = sys.argv.index("-d")
    directories_names = []
    for argument in sys.argv[index_of_d + 1:]:
        if argument.startswith("-"):
            break
        directories_names.append(argument)
    formated_directories_names = os.path.join(*directories_names)
    current_directory = os.getcwd()
    result_path = os.path.join(current_directory, formated_directories_names)
    print(result_path)
    os.makedirs(result_path, exist_ok=True)
    return result_path


def create_file(current_directory: None | str) -> None:
    index_of_f = sys.argv.index("-f")
    file_name_list = sys.argv[index_of_f + 1:]
    if current_directory is None:
        current_directory = os.getcwd()
    with open(os.path.join(current_directory, file_name_list[0]), "a") as f:
        if f.tell() > 0:
            f.write("\n")
        line_count = 1
        today = datetime.datetime.now()
        f.write(str(today.strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{line_count} " + user_input + "\n")
            line_count += 1


if "-d" in sys.argv and "-f" not in sys.argv:
    create_directories()

if "-f" in sys.argv and "-d" not in sys.argv:
    create_file(None)

if "-d" in sys.argv and "-f" in sys.argv:
    path = create_directories()
    create_file(path)
