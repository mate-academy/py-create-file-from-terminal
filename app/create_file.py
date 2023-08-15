from sys import argv
import os
import datetime


def create_directories() -> None:
    if "-d" not in argv:
        return

    if "-f" not in argv:
        dirs = (argv[argv.index("-d") + 1:])
    else:
        dirs = (argv[argv.index("-d") + 1: argv.index("-f")])

    os.makedirs(os.path.join("/".join(dirs)), exist_ok=True)
    os.chdir(os.path.join("/".join(dirs)))


def create_file() -> None:
    if "-f" not in argv:
        return

    filename = argv[argv.index("-f") + 1:][0]

    with open(filename, "a+") as file:

        date_to_write = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.seek(0)
        if file.read():
            file.write(f"\n\n{date_to_write}")
        else:
            file.write(f"{date_to_write}")

        line_counter = 0

        while True:

            content = input("Enter content line: ")
            if content == "stop":
                break

            line_counter += 1
            file.write(f"\n{line_counter} {content}")


create_directories()
create_file()
