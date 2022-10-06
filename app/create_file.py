import datetime
import os
import sys


def create_or_check_path(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"'{path}' already exists \n")


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        line_num = 1
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            user_input = input("Enter content line:")

            if user_input.lower() == "stop":
                f.write("\n")
                break

            f.write(f"{line_num} {user_input} \n")
            line_num += 1


def create_file_from_terminal() -> None:
    command = sys.argv[1:]

    if "-d" in command and "-f" not in command:
        path = "/".join(command[1:])

        create_or_check_path(path)

    elif "-f" in command and "-d" not in command:
        file_name = command[-1]
        create_file(file_name)

    elif "-f" in command and "-d" in command:
        file_name = command[-1]
        path = "/".join(command[1:-2])

        create_or_check_path(path)

        file_name = path + "/" + file_name
        create_file(file_name)


create_file_from_terminal()
