import datetime
import sys
import os


def create_file():
    terminal = sys.argv
    path = os.path.curdir
    if "-d" in terminal:
        path = "/".join(terminal[
                        terminal.index("-d") + 1:
                        terminal.index("-f")
                        if "-f" in terminal
                        else len(terminal)])
        if not os.path.exists(path):
            os.makedirs(path)
    if "-f" in terminal:
        name = terminal[terminal.index("-f") + 1]
        with open(path + "/" + name, "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                new_content = input("Enter content line, or 'stop': ")
                if new_content.lower() == "stop":
                    file.write("\n")
                    break
                file.write(f"{new_content}\n")


create_file()
