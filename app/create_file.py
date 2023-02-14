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
        context: str
) -> None:
    if os.path.exists(filename):
        with open(filename, "a") as file:
            file.write(f"\n{context}")
    else:
        with open(filename, "a") as file:
            file.write(context)


def create_directories(dir_names: list) -> None:
    os.makedirs(os.path.join(*dir_names), exist_ok=True)


def analysis_command(command_text) -> None:
    if "-f" in command_text and "-d" not in command_text:
        create_file(command_text[1], create_content())

    elif "-f" not in command_text and "-d" in command_text:
        create_directories(command_text[1:])

    elif "-f" in command_text and "-d" in command_text:
        command_text.remove("-f")
        command_text.remove("-d")
        create_directories(
            command_text[0:2]
        )
        create_file(
            os.path.join(*command_text), create_content()
        )


analysis_command(command)
