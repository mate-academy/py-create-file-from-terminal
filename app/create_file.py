import sys
import os
import datetime


# function, which create text file and fill it
def file_write(*filename) -> None:
    text = open(os.path.join(*filename), "a")
    text.write(str(datetime.datetime.now()
                   .strftime("%Y-%m-%d %H:%M%:%S")) + "\n")

    while True:
        message = input("Enter content line: ") + "\n"
        if message == "stop\n":
            break
        text.write(message)
    text.write("\n")


# function, which create dictionary
def create_dic(filesname: list) -> str:
    path = os.path.join(*filesname)
    os.makedirs(path)
    return path


def create_file() -> None:
    # take message from terminal
    terminal = sys.argv
    # check, does we need to make a directory and text file
    if "-d" in terminal and "-f" in terminal:
        text_name = terminal[terminal.index("-f") + 1]
        path = create_dic(terminal[terminal.index("-d")
                                   + 1: terminal.index("-f")]
                          or terminal[terminal.index("-d") + 1:])
        file_write(path, text_name)
    # check, does we need to make a directory
    elif "-d" in terminal:
        create_dic(terminal[terminal.index("-d") + 1:])
    # # check, does we need to make a text file
    elif "-f" in terminal:
        file_write(terminal[terminal.index("-f") + 1])


if __name__ == "__main__":
    create_file()
