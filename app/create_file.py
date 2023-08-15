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

    joined_dirs = os.path.join(*dirs)

    os.makedirs(joined_dirs, exist_ok=True)
    os.chdir(joined_dirs)


def create_file() -> None:
    if "-f" not in argv:
        return

    filename = argv[argv.index("-f") + 1:][0]
    date_to_write = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a+") as file:

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


if __name__ == "__main__":
    create_directories()
    create_file()
