import argparse
import os
import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        f.write(f"{time_now}\n")

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line}\n")


def create_dir(path: str, file_name: str) -> None:
    if path:
        full_path = os.path.join(*path)
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        if file_name:
            path_to_file = os.path.join(full_path, file_name)
            print(path_to_file)
            create_file(path_to_file)
    elif file_name:
        create_file(file_name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="filename", required=False)
    parser.add_argument("-d", dest="dir_name", nargs="+", required=False)
    args = parser.parse_args()
    create_dir(args.dir_name, args.filename)


if __name__ == "__main__":
    main()
