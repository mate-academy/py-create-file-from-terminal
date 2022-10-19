import sys

import os

from datetime import datetime


def main() -> None:
    cwd = os.getcwd()
    date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "-d" in sys.argv and "-f" not in sys.argv:
        path = os.path.join(cwd, "app", sys.argv[-2], sys.argv[-1])
        os.makedirs(path)
    if "-f" in sys.argv and "-d" not in sys.argv:
        with open(f"app/{sys.argv[-1]}", "a") as file:
            file.write(date_today + "\n")
            lines = ""
            count_lines = 0
            for line in sys.stdin:
                if "stop" == line.rstrip():
                    break
                count_lines += 1
                print(f"Enter content line: {line}")
                lines += f"{count_lines} {line}"
            file.write(f"{lines}\n")
    if "-d" in sys.argv and "-f" in sys.argv:
        path = os.path.join(cwd, "app", sys.argv[-4], sys.argv[-3])
        os.makedirs(path)
        with open(f"{path}/{sys.argv[-1]}", "w") as file:
            file.write(date_today + "\n")
            lines = ""
            count_lines = 0
            for line in sys.stdin:
                if "stop" == line.rstrip():
                    break
                count_lines += 1
                print(f"Enter content line: {line}")
                lines += f"{count_lines} {line}"
            file.write(lines)


if __name__ == "__main__":
    main()
