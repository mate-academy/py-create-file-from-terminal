import os
import sys
from datetime import datetime


def input_reader() -> list[str]:
    lines_ac = []
    while True:
        user_line = input("Enter content line: ")
        if user_line == "stop":
            break
        lines_ac.append(user_line)
    return lines_ac


def form_path(parts_to_join: list[str]) -> str:
    final_dir = "."
    if parts_to_join:
        final_dir = os.path.join(*parts_to_join)
        os.makedirs(final_dir, exist_ok=True)
    return final_dir


def parse_arguments(
        raw_args: list[str],
        base_file_name: str,
        collected_path: list[str]
) -> str:
    idx = 0
    result_name = base_file_name
    while idx < len(raw_args):
        if raw_args[idx] == "-d":
            idx += 1
            while idx < len(raw_args) and not raw_args[idx].startswith("-"):
                collected_path.append(raw_args[idx])
                idx += 1
        elif raw_args[idx] == "-f":
            if idx + 1 < len(raw_args):
                result_name = raw_args[idx + 1]
            idx += 2
        else:
            idx += 1
    return result_name


def write_into_file(
        text_lines: list[str],
        target_path: str,
        time_str: str
) -> None:
    has_content = (
        os.path.exists(target_path) and os.path.getsize(target_path) > 0
    )

    with open(target_path, "a") as file_handle:
        if has_content:
            file_handle.write("\n")

        file_handle.write(time_str + "\n")
        for i, content_line in enumerate(text_lines, 1):
            file_handle.write(f"{i} {content_line}\n")


terminal_args = sys.argv[1:]
path_parts: list[str] = []
file_name = ""

file_name = parse_arguments(terminal_args, file_name, path_parts)
directory_path = form_path(path_parts)

if file_name:
    full_file_path = os.path.join(directory_path, file_name)
    content_lines = input_reader()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_into_file(content_lines, full_file_path, timestamp)
