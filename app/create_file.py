import sys
import os
import datetime


param = sys.argv


def create_from_terminal_file(arguments: list) -> None:
    if "-d" in arguments and "-f" not in arguments:
        base_path = os.getcwd()
        for argument in arguments:
            if argument not in ["create_file.py", "-d"]:
                base_path = os.path.join(base_path, argument)
                if not os.path.exists(base_path):
                    os.makedirs(base_path)

    if "-f" in arguments and "-d" not in arguments:
        current_date = datetime.datetime.now()
        formated_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
        with open(arguments[2], "a") as file:
            file.write(formated_time + "\n")
            nums = 0
            while True:
                nums += 1
                user_input = input("Enter content line: ")
                if "stop" not in user_input:
                    file.write(f"{nums} {user_input}\n")
                if user_input == "stop":
                    file.write("\n")
                    file.close()
                    return True

    if "-d" in arguments and "-f" in arguments:
        based_path = os.getcwd()
        for argument in arguments:
            if argument not in ["create_file.py", "-d", "-f", arguments[-1]]:
                based_path = os.path.join(based_path, argument)
                if not os.path.exists(based_path):
                    os.makedirs(based_path)
        os.chdir(based_path)
        with open(arguments[5], "a") as file:
            current_date = datetime.datetime.now()
            formated_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
            file.write(formated_time + "\n")
            nums = 0
            while True:
                nums += 1
                user_input = input("Enter content line: ")
                if "stop" not in user_input:
                    file.write(f"{nums} {user_input}\n")
                if user_input == "stop":
                    file.write("\n")
                    file.close()
                    return True


create_from_terminal_file(param)
