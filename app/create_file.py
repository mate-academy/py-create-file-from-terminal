import sys
import os
from datetime import datetime


class FlagError(Exception):
    pass


class ArgumentError(Exception):
    pass


def if_flag(argument: str) -> bool:
    if argument.startswith("-"):
        return True


def main(args: list[str]) -> None:
    available_flags = ["-d", "-f"]
    flags = [flag for flag in args if if_flag(flag)]
    if not any([True if flag in available_flags else False for flag in flags]):
        raise FlagError("You must enter at least one flag")
    if not all([True if flag in available_flags else False for flag in flags]):
        raise FlagError("Invalid flags entered")
    index_dict = {}
    for flag in flags:
        index_dict[flag] = args.index(flag)
    flags_args = {}
    for flag in flags:
        flags_args[flag] = []
        for i in range(index_dict[flag] + 1, len(args)):
            if if_flag(args[i]):
                break
            flags_args[flag].append(args[i])
    base_path = ""
    if "-d" in flags:
        if len(flags_args["-d"]) == 0:
            raise ArgumentError(
                "At least one argument is required for the -d flag"
            )
        base_path = os.path.join(*flags_args["-d"])
        os.makedirs(base_path, exist_ok=True)
    if "-f" in flags:
        if len(flags_args["-f"]) == 0:
            raise ArgumentError(
                "At least one argument is required for the -f flag"
            )
        file_path = os.path.join(base_path, flags_args["-f"][0])
        input_list = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            input_list.append(line)
        with open(file_path, "w") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(current_time + "\n")
            for index, line in enumerate(input_list):
                file.write(f"{index + 1} {line}\n")


main(sys.argv)
