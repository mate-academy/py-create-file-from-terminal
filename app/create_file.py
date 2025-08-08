import os
import sys
from datetime import datetime


def create_content() -> list[str]:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def write_to_file(file_path: str, file_name: str) -> None:
    path = os.path.join(file_path, file_name)
    content = create_content()
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(content, 1):
            file.write(f"{i} Line{i} {line} \n")


def parse_args(args: list[str]) -> dict[str:list[str]]:
    result = {"-f": [], "-d": []}
    flag = None
    for arg in args:
        if arg in result:
            flag = arg
        else:
            result[flag].append(arg)
    return result


def create_directory(parts: list[str]) -> str:
    path = os.path.join(*parts)
    os.makedirs(path, exist_ok=True)
    return path


if __name__ == "__main__":
    res = parse_args(sys.argv[1:])
    path = create_directory(res["-d"])
    if res["-f"][0]:
        file_name = res["-f"][0]
        write_to_file(path, file_name)
