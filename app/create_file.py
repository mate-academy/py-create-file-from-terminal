import os
import sys
import datetime


def create_file() -> None:
    direct = sys.argv
    directories = direct[2:]

    if "-d" and "-f" in direct:
        name = []
        for word in direct[2:]:
            if word == "-f":
                break
            name.append(word)
        path_name = "/".join(name)

        if not os.path.exists(path_name):
            os.makedirs(path_name, exist_ok=True)

        name_of_txt = direct[-1]
        with open(name_of_txt, "a") as file:
            file.write(write_in_file())

    elif "-d" in direct and "-f" not in direct:
        path_name = "/".join(directories)
        if not os.path.exists(path_name):
            os.makedirs(path_name, exist_ok=True)

    elif "-f" in direct and "-d" not in direct:
        name_of_txt = direct[-1]
        if os.path.isfile(name_of_txt):
            with open(name_of_txt, "a") as file:
                file.write(write_in_file())
        else:
            with open(name_of_txt, "w") as file:
                file.write(write_in_file())


def write_in_file() -> str:
    content = []

    datetime_now = datetime.datetime.now()
    date_and_time = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

    while True:
        print("Enter content line: ")
        line = input()
        if "stop" == line.lower():
            break
        content.append(line)

    content_in_txt = [f"{i+1} {line}" for i, line in enumerate(content)]
    result = [date_and_time] + content_in_txt
    return "\n".join(result) + "\n"
