import os
import sys
import datetime


def main() -> None:
    args = sys.argv
    create_directories_and_file(args)


def create_directories_and_file(args: list[str]) -> None:
    path_to_create_file = ""
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args[d_index:]:
            f_index = args[d_index:].index("-f")
        else:
            f_index = len(args[d_index:])
        path_to_create_file = os.path.join(
            "",
            *args[d_index + 1:f_index + d_index]
        )
        os.makedirs(path_to_create_file, exist_ok=True)
    if "-f" in args:
        f_index = args.index("-f")
        create_file(path_to_create_file, args[f_index + 1])


def create_file(path: str, filename: str) -> None:
    path_to_create_file = os.path.join(path, filename)
    with open(
            path_to_create_file,
            mode_to_create_or_append_file(path_to_create_file)
    ) as file:
        row = 1
        time = datetime.datetime.now()
        if file.read():
            file.write("\n\n")
        file.write(str(time.strftime("%Y-%m-%d %H:%M:%S")))
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"\n{row} {content}")
            row += 1


def mode_to_create_or_append_file(path: str) -> str:
    return "r+" if os.path.isfile(path) else "w+"


if __name__ == "__main__":
    main()
