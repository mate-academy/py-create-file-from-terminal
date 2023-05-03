import sys
import os
import datetime


# function, which create text file and fill it
def file_write(filename: str) -> None:
    text = open(filename, "a")
    text.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M%:%S") + "\n")

    while True:
        message = input("Enter content line: ") + "\n"
        if message == "stop\n":
            break
        text.write(message)
    text.write("\n")


# function, which create dictionary
def create_dic(filesname: list) -> None:
    path = os.path.join(filesname[2], filesname[3])
    os.makedirs(path)


def create_file() -> None:
    # take message from terminal
    terminal = sys.argv
    # check, does we need to make a directory and text file
    if len(terminal) > 4:
        create_dic(terminal)
        path = os.path.join(terminal[2], terminal[3], terminal[5])
        file_write(path)
    # check, does we need to make a directory
    elif "-d" in terminal:
        create_dic(terminal)
    # # check, does we need to make a text file
    elif "-f" in terminal:
        file_write(terminal[2])


if __name__ == "__main__":
    create_file()
