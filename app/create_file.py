# write your code here
from datetime import datetime
import sys
import os


def main() -> None:
    if sys.argv[1] == "-d":
        path_to_directory = os.path.join(*sys.argv[2:])
        os.makedirs(path_to_directory, exist_ok=True)

    if sys.argv[1] == "-f":
        path_to_file = str(sys.argv[2])

        if os.path.exists(path_to_file):
            with open(path_to_file, "a") as file:
                file.write(str(datetime.now().
                               strftime("%Y-%m-%d %H:%M:%S")) + "\n")
                line = 0
                while True:
                    content = input("Enter content line: ")
                    line += 1
                    if content == "stop":
                        break
                    file.write(f"Another line{line} " + content + "\n")

        else:
            with open(path_to_file, "a") as file:
                file.write(str(datetime.now().
                               strftime("%Y-%m-%d %H:%M:%S")) + "\n")
                line = 0
                while True:
                    content = input("Enter content line: ")
                    line += 1
                    if content == "stop":
                        break
                    file.write(f"Line{line} " + content + "\n")

    if "-d" in sys.argv and "-f" in sys.argv:
        path_to_directory = os.path.join(sys.argv[2], sys.argv[3])
        os.makedirs(path_to_directory, exist_ok=True)

        path_to_file = os.path.join(path_to_directory, str(sys.argv[5]))

        with open(path_to_file, "a") as source_file:
            source_file.write(str(datetime.now().
                              strftime("%Y-%m-%d %H:%M:%S")) + "\n")
            line = 0
            while True:
                content = input("Enter content line: ")
                line += 1
                if content == "stop":
                    break
                source_file.write(f"Line{line} " + content + "\n")


if __name__ == "__main__":
    main()
