import sys
import os
import datetime


def open_write_file(file_name):
    with open(file_name, "a") as file:
        file.write(
            str(datetime.datetime.now().replace(microsecond=0)) + "\n"
        )
        line_index = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.writelines(f"{line_index} {content}\n")
            line_index += 1


def check_if_directories_in_command() -> str:
    directory = ""
    if "-d" in sys.argv:
        directory = sys.argv[sys.argv.index("-d") + 1:]
        if "-f" in directory:
            directory = directory[:directory.index("-f")]
        directory = os.path.join(*directory) + "\\"

        if os.path.dirname(directory) != "":
            os.makedirs(os.path.dirname(directory), exist_ok=True)
    return directory


def check_if_file_in_command(directory: str) -> None:
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1:]
        if "-d" in directory:
            file_name = file_name[:directory.index("-f")]
        file_name = f"{directory}" + "".join(file_name)
        open_write_file(file_name)


def main() -> None:
    directory = check_if_directories_in_command()
    check_if_file_in_command(directory)


if __name__ == "__main__":
    main()
