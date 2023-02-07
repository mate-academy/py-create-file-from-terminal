import sys
import os
import datetime


def file_creator(command: list) -> None:
    d_command = []
    print(d_command.__len__())
    f_command = ""

    check = ""

    for command_item in command[1:]:
        if command_item == "-d":
            check = command_item
            continue
        if command_item == "-f":
            check = command_item
            continue

        if check == "-d":
            d_command.append(command_item)
        if check == "-f":
            f_command += command_item

    if d_command.__len__() > 0:
        os.makedirs(os.path.join(*d_command), exist_ok=True)
        f_command = os.path.join(*d_command, f_command)

    with open(f_command, "a") as file:
        content_list = []

        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            content = input("Enter content line: ")

            if content.strip() == "stop":
                break
            content_list.append(content)

        for line in content_list:
            file.write(line + "\n")


input_from_terminal = sys.argv

file_creator(input_from_terminal)
