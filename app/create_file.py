import os
import sys
import datetime


def create_directory(directory_name: str) -> None:
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        os.chdir(directory_name)


def create_file(file_name: str) -> None:
    with open(file_name, "w") as file:
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{create_time}")

        lines = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"Line{lines}: {new_line}\n")
            lines += 1


def main() -> None:
    for index, arg in enumerate(sys.argv):
        if arg == "-d":
            create_directory(sys.argv[index + 1])

        elif arg == "-f":
            create_file(sys.argv[index + 1])


if __name__ == "__main__":
    main()
