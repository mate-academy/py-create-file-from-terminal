import argparse
import os
from datetime import datetime


def get_user_input(is_file_exist: bool = False) -> str:
    iterator = 1
    text_lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    inserted_word_if_file_exist = " Another" if is_file_exist else ""

    while True:
        user_input = input(
            f"Enter content line:{inserted_word_if_file_exist} Line{iterator} "
        )
        if user_input == "stop":
            break

        text_lines.append(
            f"{iterator}{inserted_word_if_file_exist} "
            f"Line{iterator} {user_input}"
        )
        iterator += 1
    return "\n".join(text_lines)


def write_text_to_file(
    file_path: str, file_content: str, file_mode: str = "w"
) -> None:
    with open(file_path, file_mode) as file:
        file.write(file_content)


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    path = os.getcwd()

    if args.d:
        path = os.path.join(path, *args.d)
        os.makedirs(path, exist_ok=True)

    if args.f:
        path = os.path.join(path, args.f)

        if os.path.exists(path):
            write_text_to_file(
                path,
                f"\n\n{get_user_input(is_file_exist=True)}",
                "a"
            )
        else:
            write_text_to_file(
                path,
                get_user_input()
            )


create_file()
