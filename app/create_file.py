import argparse
import os
import datetime


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        daytime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{daytime}\n")
        line = 1

        while True:
            text = input("Enter your text: ")
            if text == "stop":
                break
            file.write(f"Line{line} {text}\n")
            line += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    arg = parser.parse_args()

    if arg.directory:
        n_directory = os.path.join(*arg.directory)
        create_directory(n_directory)

    if arg.file:
        file_name = arg.file
        if arg.directory:
            os.chdir(n_directory)
        create_file(file_name)


if __name__ == "__main__":
    main()
