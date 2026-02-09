import os
import datetime

from typing import LiteralString


def file_creation(
        path: LiteralString | str | bytes,
        name: str
) -> None:
    os.makedirs(path, exist_ok=True)
    assert name,(
        "File name not found"
    )

    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(os.path.join(path, name), "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for i in range(len(content)):
            file.write(f"\n{i + 1} {content[i]}")
        file.write("\n\n")


def separate_argv(args: list) -> None:
    assert args.count("-d") == 1 and args.count("-f") == 1,(
        "Too many arguments"
    )

    d_flag = "None"
    path = os.curdir
    name = ""

    for arg in args:
        if arg == "-d":
            d_flag = "-d"
            continue
        elif arg == "-f":
            d_flag = "-f"
            continue

        if d_flag == "-d":
            path = os.path.join(path, arg)
        if d_flag == "-f":
            name = arg


    file_creation(path, name)
