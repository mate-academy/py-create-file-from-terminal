import os
import sys
import datetime

STATE_FILE = ".last_dir"


def save_dir(path: str) -> None:
    with open(STATE_FILE, "w") as f:
        f.write(path)


def load_dir() -> str:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return f.read().strip()
    return os.getcwd()


def get_command() -> None:
    data = sys.argv

    if ("-f" in data) and ("-d" in data):
        directory = data[data.index("-d") + 1 : data.index("-f")]
        file_name = data[data.index("-f") + 1]

        dir_path = os.path.join(os.getcwd(), *directory)
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, file_name)

        with open(file_path, "a") as f:
            content = input("Enter content line: ")
            counter = 1
            f.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            )

            while content != "stop":
                f.write(f"{counter} {content}\n")
                counter += 1
                content = input("Enter content line: ")

            f.write("\n")

    elif "-f" in data:
        file_name = data[data.index("-f") + 1]
        dir_path = load_dir()
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, file_name)

        with open(file_path, "a") as f:
            content = input("Enter content line: ")
            counter = 1
            f.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            )

            while content != "stop":
                f.write(f"{counter} {content}\n")
                counter += 1
                content = input("Enter content line: ")

            f.write("\n")

    else:
        directory = data[data.index("-d") + 1 :]

        dir_path = os.path.join(os.getcwd(), *directory)
        os.makedirs(dir_path, exist_ok=True)
        save_dir(dir_path)


if __name__ == "__main__":
    get_command()
