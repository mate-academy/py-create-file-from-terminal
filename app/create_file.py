import sys
import os
import datetime


def create_path(output: list) -> str:
    if output[1] != "-d" and output[-2] != "-f":
        raise ValueError("Please write your command correctly!")
    for index in range(len(output)):
        if output[index] == "-d":
            path = ""
            for dir_index in range(index + 1, len(output)):
                if output[dir_index] == "-f":
                    break
                path += output[dir_index] + "/"
            return path


def create_dir(path: str) -> None:
    os.makedirs(path)


def create_file(name: str) -> None:
    with open(f"{name}", "a") as new_file:
        new_file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        number = 0
        while True:
            number += 1
            some_input = input("Enter content line: ")
            if some_input == "stop":
                new_file.write(" \n")
                break
            new_file.write(f"{number} {some_input}\n")


if __name__ == "__main__":
    def main(output: list) -> None:
        if output[1] == "-d" and output[-2] == "-f":
            create_dir(create_path(output))
            create_file(create_path(output) + output[-1])
        elif output[1] == "-d":
            create_dir(create_path(output))
        elif output[-2] == "-f":
            create_file(output[-1])

    main(sys.argv)
