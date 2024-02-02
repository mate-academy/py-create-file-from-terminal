import os
import sys
from datetime import datetime


CMD_LIST = sys.argv[:]


def get_content() -> list[str]:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_number = 1

    while (content_line := input("Enter content line: ")) != "stop":
        content.append(f"\n{line_number} {content_line}")
        line_number += 1

    return content if len(content) > 1 else [""]


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file_to_create:
        file_to_create.writelines(get_content())
        file_to_create.write("\n\n")

    return


def main() -> None:
    if len(set(CMD_LIST)) == len(CMD_LIST):

        if CMD_LIST[1] == "-d" and "-f" not in CMD_LIST:
            path = os.path.join(*sys.argv[CMD_LIST.index("-d") + 1::])
            os.makedirs(path, exist_ok=True)

        if CMD_LIST[1] == "-f" and "-d" not in CMD_LIST:
            create_file(CMD_LIST[-1])

        if CMD_LIST[1] == "-d" and CMD_LIST[-2] == "-f":
            path = os.path.join(
                *sys.argv[CMD_LIST.index("-d") + 1:CMD_LIST.index("-f"):]
            )

            os.makedirs(path, exist_ok=True)
            create_file(os.path.join(path, CMD_LIST[-1]))


main()
