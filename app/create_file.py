import os
import sys
from datetime import datetime


def create_directory(way: list) -> None:
    path = os.path.join(*way)
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(way: str) -> None:
    if os.path.exists(way):
        with open(way, "a") as new_file:
            new_file.write("\n")

    with open(way, "a") as new_file:
        new_file.write(
            str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
        )
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            new_file.write(f"{str(count)} " + line + "\n")
            count += 1


def main() -> None:
    current_directory, flag, *expected_way = sys.argv

    if "-f" in expected_way:
        expected_way.remove("-f")
        create_directory(expected_way[:-1])
        create_file(os.path.join(*expected_way))
    if flag == "-d":
        create_directory(expected_way)
    if flag == "-f":
        create_file(*expected_way)


if __name__ == "__main__":
    main()
