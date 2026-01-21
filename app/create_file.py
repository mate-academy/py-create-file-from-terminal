import os
import sys
from _datetime import datetime

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")


def create_file() -> None:

    if "-d" in sys.argv:
        file_path = os.path.join(sys.argv[2], sys.argv[3])
        os.makedirs(file_path, exist_ok=True)
    elif "-f" in sys.argv:
        file_name = sys.argv[2]
        with open(file_name, "w") as file:
            file.write(formatted)
            print("Enter content line: ")
            while True:
                line = input()
                if line.lower() == "stop":
                    break
                file.write(line + "\n")
    elif "-d" and "-f" in sys.argv:
        file_name = sys.argv[5]
        file_path = os.path.join(sys.argv[2], sys.argv[3], file_name)
        os.makedirs(file_path, exist_ok=True)
        with open(file_name, "w") as file:
            file.write(formatted)
            print("Enter content line: ")
            while True:
                line = input()
                if line.lower() == "stop":
                    break
                file.write(line + "\n")


if __name__ == "__main__":
    create_file()
