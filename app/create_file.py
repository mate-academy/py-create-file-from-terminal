import os
import sys


def make_path() -> str:
    file_path = os.getcwd()
    file_name = "file.txt"

    index = 1
    while index < len(sys.argv):
        arg = sys.argv[index]
        if arg == "-d":
            while arg != "-f" and index < len(sys.argv):
                arg = sys.argv[index]
                file_path += f"\\{arg}"
                os.mkdir(file_path)
                index += 1
            continue
        if arg == "-f":
            file_name = sys.argv[index + 1]

    return f"{file_path}\\{file_name}"


def write_file(file_name: str) -> None:
    with open(file_name, "w") as file:
        while True:
            input_content = input("Enter content line: ")
            if input_content == "stop":
                break
            file.write(f"{input_content}\n")


def main() -> None:
    file_name = make_path()
    write_file(file_name)


if __name__ == "__main__":
    main()

