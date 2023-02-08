import sys
import os
import datetime


def file_from_terminal(command: list) -> None:
    d_command = []
    f_command = ""

    if "-d" in command and "-f" in command:
        index_d, index_f = command.index("-d"), command.index("-f")

        if index_d > index_f:
            d_command = command[index_d + 1:]
            f_command = command[index_f + 1:index_d]

        if index_d < index_f:
            d_command = command[index_d + 1:index_f]
            f_command = command[index_f + 1:]

    if "-d" in command and "-f" not in command:
        d_command = command[2:]

    if "-f" in command and "-d" not in command:
        f_command = command[2:]

    if len(d_command) > 0:
        os.makedirs(os.path.join(*d_command), exist_ok=True)

    if len(f_command) > 0:
        f_command = os.path.join(*d_command, *f_command)

        with open(f_command, "a") as file:
            content_list = []

            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

            while True:
                content = input("Enter content line: ")

                if content.strip() == "stop":
                    break

                content_list.append(content)

            for index, line in enumerate(content_list):
                file.write(f"{index + 1} {line}\n")


if __name__ == "__main__":
    input_from_terminal = sys.argv

file_from_terminal(input_from_terminal)
