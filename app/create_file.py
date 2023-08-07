from sys import argv
import os
import datetime

terminal_commands = argv

if "-d" in terminal_commands:
    if "-f" in terminal_commands:
        dirs = (
            terminal_commands[terminal_commands.index("-d") + 1:
                              terminal_commands.index("-f")]
        )
    else:
        dirs = (
            terminal_commands[terminal_commands.index("-d") + 1:]
        )

    for directory in dirs:
        if not os.path.exists(directory):
            os.mkdir(directory)

        os.chdir(directory)

if "-f" in terminal_commands:
    filename = terminal_commands[terminal_commands.index("-f") + 1:][0]

    with open(filename, "a") as file:

        with open(filename, "r") as file_check_is_empty:
            if file_check_is_empty.read():
                file.write("\n")

        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        line_counter = 0

        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            line_counter += 1
            file.write(f"{line_counter} {content}\n")
