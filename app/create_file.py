import sys
import os
import datetime


def file_write(*filename: tuple[str]) -> None:
    text = open(os.path.join(*filename), "a")
    text.write(
        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M%:%S")) + "\n"
    )

    while True:
        message = input("Enter content line: ") + "\n"
        if message == "stop\n":
            break
        text.write(message)
    text.write("\n")


def create_directories(file_name: list[str]) -> str:
    path = os.path.join(*file_name)
    os.makedirs(path)
    return path


def create_file() -> None:
    terminal = sys.argv
    if "-d" in terminal and "-f" in terminal:
        text_name = terminal[terminal.index("-f") + 1]
        path = create_directories(
            terminal[terminal.index("-d") + 1: terminal.index("-f")]
            or terminal[terminal.index("-d") + 1:]
        )
        file_write(path, text_name)
    elif "-d" in terminal:
        create_directories(terminal[terminal.index("-d") + 1 :])
    elif "-f" in terminal:
        file_write(terminal[terminal.index("-f") + 1])


if __name__ == "__main__":
    create_file()
