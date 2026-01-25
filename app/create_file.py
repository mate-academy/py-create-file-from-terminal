import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Please provide arguments. "
              "Use -d for directories and/or -f for "
              "filename.")
        return

    dir_parts = []
    filename = None

    if "-d" in args:
        d_idx = args.index("-d")
        if "-f" in args:
            f_idx = args.index("-f")
            if d_idx < f_idx:
                dir_parts = args[d_idx + 1:f_idx]
            else:
                dir_parts = args[d_idx + 1:]
        else:
            dir_parts = args[d_idx + 1:]

    if "-f" in args:
        f_idx = args.index("-f")
        if f_idx + 1 < len(args):
            filename = args[f_idx + 1]

    target_dir = ""
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)
        print(f"Directory created/verified: {target_dir}")

    if filename:
        full_path = os.path.join(target_dir, filename) \
            if target_dir else filename

        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(full_path, "a", encoding="utf-8") as file:
            file.write(f"{timestamp}\n")
            for i, line in enumerate(lines, 1):
                file.write(f"{i} {line}\n")

        print(f"\nSuccessfully written to {full_path}")


if __name__ == "__main__":
    main()
