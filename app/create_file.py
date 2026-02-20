import sys
import os
import datetime
from types import TracebackType
from typing import TextIO


class FileManager:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.f = TextIO

    def __enter__(self) -> TextIO:
        self.f = open(self.filename, self.mode, encoding="utf-8")
        return self.f

    def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None) -> bool | None:
        self.f.close()


def main() -> None:
    path: str = os.getcwd()
    filename: str = ""
    args: list[str] = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            dirs = []
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            if dirs:
                path = os.path.join(path, *dirs)
                os.makedirs(path, exist_ok=True)
                continue
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: missing filename")
                return
        else:
            i += 1

    if not filename:
        print("Error: No filename specified. Use '-f' to specify a filename.")
        return

    fullpath = os.path.join(path, filename)

    try:
        with FileManager(fullpath, mode="a") as f:
            count = 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            while True:
                line = input("Enter content line: ")
                if line.strip().lower() == "stop":
                    break
                f.write(f"{count}. {line}\n")
                count += 1
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
