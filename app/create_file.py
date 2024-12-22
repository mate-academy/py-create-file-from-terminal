import sys
import os
from datetime import datetime


def parse_cli_args(cli_args: list[str]) -> tuple[str, str]:
    if "-f" not in cli_args and "-d" not in cli_args:
        raise ValueError("No -f or -d flag provided")

    dirs = ""
    if "-d" in cli_args:
        for i in range(cli_args.index("-d") + 1, len(cli_args)):
            if cli_args[i] == "-f":
                break
            dirs = os.path.join(dirs, cli_args[i])

    file_name = ""
    if "-f" in cli_args:
        flag_index = cli_args.index("-f")
        if flag_index < len(cli_args) - 1:
            file_name = cli_args[flag_index + 1]

    if not dirs and not file_name:
        raise ValueError("Must provide dirs after -d or filename after -f")

    return dirs, file_name


def take_user_input() -> list[str]:
    user_lines = []
    line_count = 1
    while True:
        user_line = input("Enter content line: ")
        if user_line == "stop":
            break
        user_lines.append(f"{line_count} {user_line}\n")
        line_count += 1

    return user_lines


def create_file_with_lines(
        file_path: str,
        timestamp: str,
        lines: list[str],
) -> None:
    if os.path.exists(file_path):
        timestamp = "\n" + timestamp

    lines = [timestamp + "\n"] + lines

    with open(file_path, "a") as file:
        file.writelines(lines)


def main(cli_args: list[str]) -> None:
    try:
        dirs, file = parse_cli_args(cli_args)
    except ValueError as e:
        print(f"Failed to parse cli args {cli_args}")
        print(e)
        return

    if dirs:
        os.makedirs(dirs, exist_ok=True)

    if file:
        file_path = os.path.join(dirs, file)

        user_input = take_user_input()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        create_file_with_lines(
            file_path,
            timestamp=current_time,
            lines=user_input
        )


if __name__ == "__main__":
    main(sys.argv)
