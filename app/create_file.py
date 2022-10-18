from datetime import datetime
from sys import argv
from os import mkdir, chdir

filename = ""
directories = []
create = True


def create_file() -> None:
    if "-d" in argv:
        index = 2
        while len(argv) != index and argv[index] != "-f":
            mkdir(argv[index])
            chdir(argv[index])
            index += 1
    if "-f" in argv:
        with open(argv[-1], "w") as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date}\n")
            line = 1
            content = input("Enter content line: ")
            while content != "stop":
                file.write(f"Line{line} {content}")
                content = input("Enter content line: ")
                line += 1


if __name__ == "__main__":
    create_file()
