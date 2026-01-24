import sys
import os
from datetime import datetime

def main():
    print("ARGS:", sys.argv)

    filename = None
    if "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f") + 1]

    if not filename:
        print("No file name")
        return

    print("Creating file:", filename)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        for i, l in enumerate(lines, 1):
            f.write(f"{i} {l}\n")


if __name__ == "__main__":
    main()
