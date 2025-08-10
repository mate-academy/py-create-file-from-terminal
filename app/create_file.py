import argparse

from pathlib import Path
from datetime import datetime


def work_with_console_flags() -> dict:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-d", "--directory",
        action="store",
        help="path to directory"
    )
    arg_parser.add_argument("-f", "--file", help="file name")
    args = arg_parser.parse_args()
    return {"path": args.directory, "name": args.file}


def file_filling_process(full_path: str) -> None:
    with open(f"{full_path}.txt", "a") as input_file:
        input_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_numb = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input.strip().lower() == "stop":
                input_file.write("\n")
                break
            input_file.write(f"{line_numb} {user_input}\n")
            line_numb += 1


def main() -> str:
    flags = work_with_console_flags()

    if all(flags.values()):
        Path(flags["path"]).mkdir(parents=True, exist_ok=True)
        file_filling_process(f"{flags['path']}/{flags['name']}")
        return f"{flags['path']}/{flags['name']} was created"

    if flags["name"]:
        file_filling_process(flags["name"])
        return f"{flags['name']} was created"

    if flags["path"]:
        Path(flags["path"]).mkdir(parents=True, exist_ok=True)
        return f"{flags['path']}/ was created"


if __name__ == "__main__":
    print(main())
