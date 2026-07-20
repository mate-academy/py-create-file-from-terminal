import sys
import os
from datetime import datetime

def main():
    args = sys.argv[1:]
    has_d = "-d" in args
    has_f = "-f" in args
    d_index = args.index("-d") if has_d else -1
    f_index = args.index("-f") if has_f else -1
    dirs = []
    if has_d:
        if has_f:
            if d_index < f_index:
                dirs = args[d_index + 1:f_index]
            else:
                dirs = args[d_index + 1:]
        else:
            dirs = args[d_index + 1:]
    dir_path = os.path.join(*dirs) if dirs else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if has_d and not has_f:
        return 0  # Замість sys.exit(0)
    if has_f:
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            file_name = "output.txt"
    else:
        file_path = "output.txt"
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")
    return 0

if __name__ == "__main__":
    main()