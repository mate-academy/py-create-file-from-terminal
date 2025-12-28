import argparse
import os
import datetime


def take_arguments_from_terminal() -> dict[str, str | list[str]]:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--directories", nargs="+", required=False)
    parser.add_argument("-f", "--file", required=False)

    args = parser.parse_args()

    result = {}
    if args.directories:
        result["directories"] = args.directories
    if args.file:
        result["file"] = args.file

    return result


def create_file(
        args: dict[str, str | list[str]],
        directory_path: str = os.getcwd()
) -> None:
    file_path = os.path.join(directory_path, args.get("file"))

    with open(file_path, "w") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        idx = 1

        while True:
            content_line = input("Enter content line: ")
            if content_line.strip().lower() == "stop":
                break
            file.write(f"{idx} {content_line}\n")
            idx += 1


def create_directory(args: dict[str, str | list[str]]) -> str:
    directory_path = os.getcwd()

    for arg in args.get("directories"):
        directory_path = os.path.join(directory_path, arg)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        else:
            print(f"Directory {directory_path} already exists")

    return directory_path


def create_file_inside_directory(args: dict[str, str | list[str]]) -> None:
    directory_path = create_directory(args)
    create_file(args, directory_path)


if __name__ == "__main__":
    arguments = take_arguments_from_terminal()

    if "directories" in arguments and "file" in arguments:
        create_file_inside_directory(arguments)
    elif "directories" in arguments:
        create_directory(arguments)
    elif "file" in arguments:
        create_file(arguments)
    else:
        print("No arguments were presented")
