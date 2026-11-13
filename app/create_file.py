import os
import sys
from datetime import datetime


def main() -> None:
    dirs = []
    file_name = None
    current_flag = None

    for arg in sys.argv[1:]:
        if arg in ("-d", "-f"):
            current_flag = arg
        elif current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f" and file_name is None:
            file_name = arg

    path = os.path.join(*dirs) if dirs else ""
    if path:
        os.makedirs(path, exist_ok=True)

    if file_name:
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = [timestamp] + [
            f"{number} {line}" for number, line in enumerate(lines, 1)
        ]

        target = os.path.join(path, file_name)
        separator = "\n" if os.path.exists(target) else ""

        with open(target, "a", encoding="utf-8") as file:
            file.write(separator + "\n".join(entry) + "\n")


main()
