import sys
import os
import datetime

command = sys.argv[1:]


def create_content() -> str:
    content = f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n"
    count = 0
    while True:
        count += 1
        line = input("Enter content line: ")
        if line == "stop":
            break
        content += f"{count} {line}\n"
    return content


def create_file(
        filename: str,
        regime: str,
        context: str
) -> None:
    with open(filename, regime) as file:
        file.write(context)


def create_directories(dir_names: list) -> None:
    os.makedirs(os.path.join(*dir_names))


if "-f" in command and "-d" not in command:
    file_name = command[1]
    if os.path.exists(file_name):
        create_file(file_name, "a", f"\n{create_content()}")
    else:
        create_file(file_name, "w", create_content())

elif "-f" not in command and "-d" in command:
    create_directories(command[1:])

elif "-f" in command and "-d" in command:
    create_directories(
        command[(command.index("-d") + 1):command.index("-f")]
    )
    command.remove("-f")
    command.remove("-d")
    create_file(
        os.path.join(*command), "w", create_content()
    )
