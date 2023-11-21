# write your code here
from datetime import datetime
import sys
import os


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        file.write(str(datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        line = 0
        while True:
            content = input("Enter content line: ")
            line += 1
            if content == "stop":
                break
            file.write(f"{line} " + content + "\n")
            file.write("\n")


def main() -> None:
    if sys.argv[1] == "-d":
        if "-f" not in sys.argv:
            path_to_directory = os.path.join(*sys.argv[2:])
            os.makedirs(path_to_directory, exist_ok=True)
        elif "-f" in sys.argv:
            path_to_file = os.path.join(sys.argv[2], sys.argv[3], sys.argv[5])
            create_file(path_to_file)

    if sys.argv[1] == "-f":
        path_to_file = str(sys.argv[2])
        create_file(path_to_file)


if __name__ == "__main__":
    main()
