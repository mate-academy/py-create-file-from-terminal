# write your code here
from datetime import datetime
import sys
import os


def create_directory(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def collect_user_input() -> list[str]:
    lines = []
    line_numbers = 0

    while True:
        input_user = input("Enter content line: ")
        if input_user.lower() == "stop":
            break
        line_numbers += 1
        lines.append(f"{line_numbers} {input_user}\n")

    return lines


def create_in_file(file_name: str) -> None:
    lines = collect_user_input()

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y.%m.%d %H:%M:%S\n"))
        file.writelines(lines)
        file.write("\n")


def parse_args(args: list) -> dict:
    new_dict = {"-d": [], "-f": None}
    if "-f" in args.index("-f"):
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            new_dict["-f"] = args[f_index + 1]

    if "-d" in args.index("-d"):
        d_index = args.index("-d")
        new_dict["-d"] = args[d_index + 1:
                              args.index("-f") if "f" in args
                              and args.index("-f") > d_index else len(args)]

    return new_dict


def main() -> None:
    directories, file_name = parse_args(sys.argv[1:])

    if directories:
        create_directory(directories)
        if file_name:
            full_name = os.path.join(*directories, file_name)
            create_in_file(full_name)
    elif file_name:
        create_in_file(file_name)


if __name__ == "__main__":
    main()
