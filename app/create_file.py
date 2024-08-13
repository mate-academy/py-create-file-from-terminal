import argparse
import os
import datetime


def create_file(file_name: str, directory_name: str = None) -> None:
    if directory_name:
        os.makedirs(directory_name, exist_ok=True)
        os.chdir(directory_name)

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

        file.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    directory_name = os.path.join(*args.directory) if args.directory else None
    file_name = args.file

    if file_name:
        create_file(file_name, directory_name)


if __name__ == "__main__":
    main()
