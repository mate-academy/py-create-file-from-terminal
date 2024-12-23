import os
import sys
import datetime
import argparse


def create_directory(directory_path: str = "") -> None:
    try:
        if not directory_path:
            directory_path = os.path.join(*sys.argv[2:])
        os.makedirs(directory_path, exist_ok=True)
    except Exception as e:
        print(e)


def create_file(file_name: str = "", directory_path: str = "") -> None:
    try:
        if not file_name:
            file_name = sys.argv[2]
        if os.path.exists(os.path.join(directory_path, file_name)):
            open(os.path.join(directory_path, file_name), "a").write("\n")
        with open(os.path.join(directory_path, file_name), "a") as file:
            line_counter = 1
            current_date = datetime.datetime.now()
            file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                file.write(f"{line_counter} {text}\n")
                line_counter += 1
    except Exception as e:
        print(e)


def create_directory_and_file() -> None:
    directory_path = os.path.join(*" ".join(sys.argv).split("-d")[1]
                                  .split("-f")[0].strip().split())
    file_name = " ".join(sys.argv).split()[-1]
    create_directory(directory_path)
    create_file(file_name, directory_path)


def main() -> None:

    parser = argparse.ArgumentParser(description="Script to receive file path and file name")
    parser.add_argument("-d", "--direction", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    flags = ["-d", "-f"]
    if all(flag in sys.argv for flag in flags):
        create_directory_and_file()
    elif sys.argv[1] == "-d":
        create_directory()
    elif sys.argv[1] == "-f":
        create_file()


if __name__ == "__main__":
    main()
