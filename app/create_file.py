import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:

    dir_parts: List[str] = []
    file_name: Optional[str] = None
    i = 0

    while i < len(argv):
        arg = argv[i]
        if arg == "-d":
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
            continue
        elif arg == "-f":
            if i + 1 < len(argv) and not argv[i + 1].startswith("-"):
                file_name = argv[i + 1]
                i += 2
                continue
            else:
                raise ValueError("Після -f очікується ім’я файлу")
        else:
            i += 1

    return dir_parts, file_name


def read_lines_until_stop() -> List[str]:
    lines: List[str] = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def write_with_timestamp(path: str, lines: List[str]) -> None:
    if not lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n" + "\n".join(lines) + "\n"

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            f.write("\n")
        f.write(content)


def main() -> None:
    dir_parts, file_name = parse_args(sys.argv[1:])

    if not dir_parts and not file_name:
        return

    dir_path = os.path.join(*dir_parts) if dir_parts else ""

    # if dir_path:
    #     os.makedirs(dir_path, exist_ok=True)

    if file_name:
        full_path = (
            os.path.join(dir_path, file_name)
            if dir_path else file_name
        )
        lines = read_lines_until_stop()
        write_with_timestamp(full_path, lines)
    else:
        return


if __name__ == "__main__":
    main()
