import argparse
from datetime import datetime
import os


def append_content(file_name: str) -> None:
    lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(f"{line_number} {content}")
        line_number += 1
    with open(file_name, "a+", encoding="utf-8") as output:
        output.seek(0)
        previous_content = output.read()
        if previous_content:
            output.write("\n" if previous_content.endswith("\n") else "\n\n")
        output.write("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", default=[])
    parser.add_argument("-f")
    arguments = parser.parse_args()
    directory = os.path.join(*arguments.d) if arguments.d else ""
    if directory:
        os.makedirs(directory, exist_ok=True)
    if arguments.f:
        append_content(os.path.join(directory, arguments.f))


if __name__ in ("__main__", "<run_path>"):
    main()
