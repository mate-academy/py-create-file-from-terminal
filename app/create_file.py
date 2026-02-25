import sys
import os
from datetime import datetime


def parse_arguments(
        args_list: list[str]
) -> tuple[str, str, bool]:
    directory_path = "."
    file_name = "file.txt"
    has_f_flag = False

    if "-f" in args_list:
        has_f_flag = True
        f_idx = args_list.index("-f")
        if f_idx + 1 < len(args_list):
            file_name = args_list[f_idx + 1]

    if "-d" in args_list:
        d_idx = args_list.index("-d")
        parts = []
        for arg in args_list[d_idx + 1:]:
            if arg == "-f":
                break
            parts.append(arg)

        if parts:
            directory_path = os.path.join(*parts)

    return directory_path, file_name, has_f_flag


def get_user_content() -> list[str]:
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        lines.append(user_input)
    return lines


def write_to_file(full_path: str, lines: list[str]) -> None:
    is_new_file = (not os.path.exists(full_path)
                   or os.path.getsize(full_path) == 0)

    with open(full_path, "a", encoding="utf-8") as output_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if is_new_file:
            output_file.write(f"{timestamp}\n")
        else:
            output_file.write(f"\n{timestamp}\n")

        for idx, text in enumerate(lines, 1):
            output_file.write(f"{idx} {text}\n")


def main() -> None:
    directory_path, file_name, has_f_flag = parse_arguments(sys.argv)

    if directory_path != ".":
        os.makedirs(directory_path, exist_ok=True)

    if has_f_flag:
        full_path = os.path.join(directory_path, file_name)
        lines = get_user_content()

        if lines:
            write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
