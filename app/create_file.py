from __future__ import annotations
import sys
import os
import datetime


def create_path(output: list) -> str | None:
    if "-f" not in output and "-d" not in output:
        raise ValueError("Please write your command correctly!")
    path = ""
    if "-f" in output and output.index("-f") > output.index("-d"):
        path = os.path.join(*output[output.index("-d") + 1:output.index("-f")])
    elif "-d" in output or output.index("-f") < output.index("-d"):
        path = os.path.join(*output[output.index("-d") + 1:])
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
    def main(input: list) -> None:
        if "-d" not in input:
            create_file(input[input.index("-f") + 1])
            return
        dir_path = create_path(input)
        os.makedirs(dir_path)
        if "-f" not in input:
            return
        else:
            create_file(os.path.join(dir_path, input[input.index("-f") + 1]))

    main(sys.argv)
