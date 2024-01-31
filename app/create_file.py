import os
from datetime import datetime
import sys


def get_content() -> list[str]:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_number = 1

    while (x := input("Enter content line: ")) != "stop":
        content.append(f"\n{line_number} {x}")
        line_number += 1

    return content if len(content) > 1 else [""]


def main() -> None:

    if "-d" in sys.argv[:]:
        if "-f" in sys.argv[:]:
            path = os.path.join(
                *sys.argv[sys.argv[:].index("-d") + 1:sys.argv[:].index("-f"):]
            )
            os.makedirs(path)
            with open(os.path.join(path, sys.argv[-1]), "a") as f:
                f.writelines(get_content())
                f.write("\n")
                f.write("\n")

            return

        path = os.path.join(*sys.argv[sys.argv[:].index("-d") + 1::])
        os.makedirs(path)

    if sys.argv[1] == "-f":
        with open(sys.argv[2], "a") as f:
            f.writelines(get_content())
            f.write("\n")
            f.write("\n")
