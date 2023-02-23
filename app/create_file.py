import datetime
import os
import sys


def create_file(file_name: str) -> None:
    lines_to_write = []
    if os.path.exists(file_name):
        lines_to_write.append("\n")
    lines_to_write.append(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    count = 1
    while (line := input("Enter content line: ")) != "stop":
        lines_to_write.append(f"{count} " + line)
        count += 1
    with open(file_name, "a") as writer:
        writer.write("\n".join(lines_to_write))


def main() -> None:
    file_path = []
    flag = None
    for arg in sys.argv[1:]:
        if arg in ("-d", "-f"):
            flag = arg
        elif flag:
            file_path.append(arg)
            if flag == "-f":
                if len(file_path) > 1:
                    os.makedirs(os.path.join(*file_path[:-1]), exist_ok=True)
                create_file(os.path.join(*file_path))


main()
