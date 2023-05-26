import sys
import os
from datetime import datetime


class FlagError(Exception):
    """An exception that occurs when there is an error related to flags."""
    pass


class ArgumentError(Exception):
    """Exception that occurs when there is
     an error related to command line arguments."""
    pass


def is_flag(argument: str) -> bool:
    if argument.startswith("-"):
        return True


def validate_flags(available_flags: list, flags: list) -> None:
    if not any([flag in available_flags for flag in flags]):
        raise FlagError("You must enter at least one flag")
    if not all([flag in available_flags for flag in flags]):
        raise FlagError("Invalid flags entered")


def parse_flags(args: list) -> list[str]:
    return [flag for flag in args if is_flag(flag)]


def main(args: list[str]) -> None:
    available_flags = ["-d", "-f"]
    flags = parse_flags(args)

    validate_flags(available_flags, flags)

    index_dict = {}
    for flag in flags:
        index_dict[flag] = args.index(flag)

    flags_args = {}
    for flag in flags:
        flags_args[flag] = []
        for i in range(index_dict[flag] + 1, len(args)):
            if is_flag(args[i]):
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

        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(current_time + "\n")
                for index, line in enumerate(input_list):
                    file.write(f"{index + 1} {line}\n")
        with open(file_path, "a") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write("\n")
            file.write(current_time + "\n")
            for index, line in enumerate(input_list):
                file.write(f"{index + 1} {line}\n")


if __name__ == "__main__":
    main(sys.argv)
