import sys
import os


def process_file_name_from_args() -> (str, str):
    path = os.getcwd()
    file_name = "file.txt"

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "-d":
            i += 1
            while arg != "-f" and i < len(sys.argv):
                arg = sys.argv[i]
                path += f"\\{arg}"
                os.mkdir(path)
                i += 1
            continue
        if arg == "-f":
            file_name = sys.argv[i + 1]
    return f"{path}\\{file_name}"


def write_file(file_name: str) -> None:
    with open(file_name, "w") as file:
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{user_input}\n")


def main() -> None:
    file_name = process_file_name_from_args()
    write_file(file_name)


if __name__ == "__main__":
    main()
