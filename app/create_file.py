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


def create_file(file_name: str, directory_name: str) -> None:
    if directory_name:
        os.makedirs(directory_name, exist_ok=True)
        os.chdir(directory_name)

    lines = collect_user_input()
    try:
        with open(file_name, "a") as file:
            file.writelines(lines)
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+", required=True)
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()

    directory_name = os.path.join(*args.directory)
    file_name = args.file

    create_file(file_name, directory_name)


if __name__ == "__main__":
    main()
