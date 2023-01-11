import sys
import os
import datetime


def create_path(output: list) -> str:
    if "-f" not in output and "-d" not in output:
        raise ValueError("Please write your command correctly!")
    for index, command in enumerate(output):
        if output[index] == "-d":
            path = ""
            for dir_index in range(index + 1, len(output)):
                if output[dir_index] == "-f":
                    break
                path += output[dir_index] + "/"
            return path


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
        path = create_path(output)
        if "-d" in output and "-f" in output:
            os.makedirs(path)
            create_file(path + output[output.index("-f") + 1])
        elif "-d" in output and "-f" not in output:
            os.makedirs(path)
        elif "-f" in output and "-d" not in output:
            create_file(output[output.index("-f") + 1])


    main(sys.argv)
