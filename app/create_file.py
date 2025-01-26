import sys
import os
from datetime import datetime


def main() -> None:
    dirs, filename = [], None
    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "-d":
            dirs.extend(arg for arg in args[i + 1:] if not arg.startswith("-"))
            i += len(dirs) + 1
        elif args[i] == "-f":
            filename = args[i + 1] if i + 1 < len(args) else None
            i += 2
        else:
            i += 1

    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)

    if filename:
        file_path = os.path.join(*dirs, filename) if dirs else filename
        prepend_newline = (
            os.path.exists(file_path) and os.path.getsize(file_path) > 0
        )

        with open(file_path, "a") as f:
            if prepend_newline:
                f.write("\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")

            input_iter = iter(lambda: input("Enter content line: "), "stop")
            for count, line in enumerate(input_iter, 1):
                f.write(f"{count} {line}\n")


if __name__ == "__main__":
    main()
