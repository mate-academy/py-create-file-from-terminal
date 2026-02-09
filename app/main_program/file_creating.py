import os
import datetime

from typing import LiteralString


def file_creation(
        path: LiteralString | str | bytes,
        name: str
) -> None:
    os.makedirs(path, exist_ok=True)
    if not name:
        return

    content = []
    while True:
        line = input(f"Enter content line: ")
        if line == "stop".lower():
            break
        content.append(line)

    with open(os.path.join(path, name), 'a') as file:
        file.write(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
        for i in range(len(content)):
            file.write(f"\n{i + 1} {content[i]}")
        else:
            file.write("\n\n")


def separate_argv(args: list) -> None:
    d_flag = False
    path = os.curdir
    name = args[args.index("-f") + 1] if args.count("-f") else ""

    for i in range(len(args)):
        if args[i - 1] == "-d":
            d_flag = not d_flag
        elif args[i] == "-f":
            d_flag = False

        if d_flag:
            path = os.path.join(path, args[i])

    file_creation(path, name)
