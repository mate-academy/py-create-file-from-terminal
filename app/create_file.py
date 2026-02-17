import datetime
import sys
import os


def parse_args() -> None:
    directory_path = []
    f_argument = False
    d_argument = False
    for argument in sys.argv:
        if argument == "-d":
            d_argument = True
            f_argument = False

        if argument == "-f":
            f_argument = True
            d_argument = False

        if d_argument and argument != "-d":
            directory_path.append(argument)
            make_dir(directory_path)

        if f_argument and argument != "-f":
            write_to_file(
                os.path.join(*directory_path, argument), collect_content()
            )
            f_argument = False


def make_dir(directory_path: list) -> None:
    os.makedirs(os.path.join(*directory_path), exist_ok=True)


def collect_content() -> str:
    text_for_file = ""
    string_count = 1
    while True:
        next_string = input("Enter content line: ")
        if next_string == "stop":
            break
        text_for_file += f"{string_count} {next_string}\n"
        string_count += 1

    date_format = "%Y-%m-%d %H:%M:%S"
    return f"{datetime.datetime.now().strftime(date_format)}\n{text_for_file}"


def write_to_file(file_path: str, text_for_file: str) -> None:
    if os.path.exists(file_path):
        text_for_file = f"\n{text_for_file}"
        with open(file_path, "a") as file:
            file.write(text_for_file)
    else:
        with open(file_path, "w") as file:
            file.write(text_for_file)


if __name__ == "__main__":
    parse_args()
