# write your code here
from datetime import datetime
import sys
import os


def create_file(path_to_file: str, line: str) -> None:
    with open(path_to_file, "a") as file:
        file.write(str(datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        line_count = 0
        while True:
            content = input("Enter content line: ")
            line_count += 1
            if content == "stop":
                break
            file.write(f"{line}{line_count} " + content + "\n")


def main() -> None:
    if sys.argv[1] == "-d":
        path_to_directory = os.path.join(*sys.argv[2:])
        os.makedirs(path_to_directory, exist_ok=True)

    if sys.argv[1] == "-f":
        path_to_file = str(sys.argv[2])

        if os.path.exists(path_to_file):
            line = "Another line"
            create_file(path_to_file, line)

        else:
            line = "Line"
            create_file(path_to_file, line)

    if "-d" in sys.argv and "-f" in sys.argv:
        path_to_directory = os.path.join(sys.argv[2], sys.argv[3])
        os.makedirs(path_to_directory, exist_ok=True)

        path_to_file = os.path.join(path_to_directory, str(sys.argv[5]))
        line = "Line"
        create_file(path_to_file, line)


if __name__ == "__main__":
    main()
