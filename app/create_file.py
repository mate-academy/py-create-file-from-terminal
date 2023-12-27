import os
import sys
from datetime import datetime


def main() -> None:
    if "-d" in sys.argv:
        directory_path_list: list[str] = sys.argv[-~sys.argv.index("-d"):]
        directory_path: str = os.path.join(
            *directory_path_list[:directory_path_list.index("-f")]
            if "-f" in directory_path_list else directory_path_list
        )
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        file_name: str = sys.argv[-~sys.argv.index("-f")]
        file_path: str = os.path.join(directory_path, file_name
                                      ) if "-d" in sys.argv else file_name

        with open(file_path, "a") as file:
            file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
            file.write(
                "".join(f"{-~counter} {line}\n" for counter, line in
                        enumerate(iter(lambda: input("Enter content line: ")
                                       , "stop"))))


if __name__ == "__main__":
    main()
