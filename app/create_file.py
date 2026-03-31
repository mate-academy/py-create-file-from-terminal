import sys
import os
from datetime import datetime


class CommandNotFound(Exception):
    pass


def main() -> None:
    argv = sys.argv
    print(sys.argv)

    if "-f" in argv:
        file_path = argv[-1]
        argv = argv[:-2]
        print(file_path)
        print(argv)
    else:
        raise CommandNotFound(
            "Usage: python create_file.py [-d dir1 dir2 ...] [-f filename.txt]"
        )

    if "-d" in argv:
        dir_index = argv.index("-d") + 1
        print(dir_index)
        dir_path = os.path.join(*argv[dir_index:])
        print(dir_path)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_path)
        print(file_path)

    with open(file_path, "a") as source_file:
        source_file.write(f"{datetime.now()}\n")
        line_num = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{line_num} {content}\n")
            line_num += 1
        print("OK")


if __name__ == "__main__":
    main()
