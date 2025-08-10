import os
import sys
from datetime import datetime
from typing import List


def create_file(
        directory_path: str,
        file_name: str,
        content: List[str]
) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_name)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n" + timestamp + "\n")
    else:
        with open(file_path, "w") as file:
            file.write(timestamp + "\n")

    with open(file_path, "a") as file:
        for line_number, line in enumerate(content, start=1):
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")


def main() -> None:
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        flag = args[0]

        if flag == "-d":
            directory_path = os.path.join(*args[1:])
            os.makedirs(directory_path)

        elif flag == "-f":
            file_name = args[1]
            content = []
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                content.append(line)
            create_file(os.getcwd(), file_name, content)


if __name__ == "__main__":
    main()
