import os
import sys
import datetime

command = sys.argv


def make_directory(commands: list) -> None:
    if len(commands) < 2:
        raise IndexError

    if "-d" in commands and "-f" in commands:
        cwd = os.getcwd()
        path_list = commands[2:-2]
        all_path = os.path.join(cwd, *path_list)
        os.makedirs(all_path, exist_ok=True)

        path_for_create_file_in_directory = os.path.join(all_path,
                                                         commands[-1])
        with open(path_for_create_file_in_directory, "a") as created_file:
            contain = []
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                contain.append(f"Enter content line: {text}")
            current_date = datetime.datetime.now()
            data = current_date.strftime("%Y-%m-%d %H:%M:%S")
            contain = [f"{i + 1} {line}" for i, line in enumerate(contain)]
            datas = str(data)
            my_list = datas + "\n" + "\n".join(contain) + "\n"

            created_file.write(my_list)

    elif commands[1] == "-d":
        cwd = os.getcwd()
        path_list = commands[2:]
        all_path = os.path.join(cwd, *path_list)
        os.makedirs(all_path, exist_ok=True)

    elif commands[1] == "-f":
        with open(commands[2], "a") as created_file:
            contain = []
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                contain.append(f"Enter content line: {text}")
            current_date = datetime.datetime.now()
            data = current_date.strftime("%Y-%m-%d %H:%M:%S")
            contain = [f"{i + 1} {line}" for i, line in enumerate(contain)]
            datas = str(data)
            my_list = datas + "\n" + "\n".join(contain) + "\n"

            created_file.write(my_list)


making = make_directory(command)
