import argparse
import os
import datetime


def collect_user_input() -> list[str]:
    lines = []
    daytime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"{daytime}\n")
    line_num = 1
    while True:
        text = input("Enter your text: ")
        if text == "stop":
            break
        lines.append(f"{line_num} Line{line_num} {text}\n")
        line_num += 1
    lines.append("\n")
    return lines


def create_file(file_name: str) -> None:
    lines = collect_user_input()
    try:
        with open(file_name, "a") as file:
            file.writelines(lines)
    except OSError as e:
        print(f"Error: {e}")


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    if args.directory:
        directory_name = os.path.join(*args.directory)
        create_directory(directory_name)
        if args.file:
            os.chdir(directory_name)
            create_file(args.file)
    elif args.file:
        create_file(args.file)


if __name__ == "__main__":
    main()
