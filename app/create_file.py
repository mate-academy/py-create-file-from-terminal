import sys
import os
import datetime


def create_directory(path_parts: list[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        file.write(date)
        while True:
            line_of_content = input("Enter content line: ") + "\n"
            if line_of_content == "stop\n":
                break
            file.write(line_of_content)
        file.write("\n")


def main() -> None:
    arguments = sys.argv
    if "-d" in arguments and "-f" in arguments:
        file_name = arguments[arguments.index("-f") + 1]
        path = create_directory(
            arguments[arguments.index("-d") + 1: arguments.index("-f")]
        )
        create_file(file_name=file_name, path=path)

    elif "-d" in arguments:
        create_directory(arguments[arguments.index("-d") + 1:])

    elif "-f" in arguments:
        create_file(file_name=arguments[arguments.index("-f") + 1])


if __name__ == "__main__":
    main()
