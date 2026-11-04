import os
import sys
import datetime


def main() -> None:
    args = sys.argv
    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None
    if d_index is not None and f_index is not None and f_index > d_index:
        dirs = args[d_index + 1:f_index]
    elif d_index is not None:
        dirs = args[d_index + 1:]
    else:
        dirs = []
    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)
    if f_index is None:
        return
    file_path = os.path.join(*dirs, args[f_index + 1])
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as file:
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line + "\n")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if file_exists:
            file.write("\n")
        file.write(current_time + "\n")
        for number, line in enumerate(lines, 1):
            file.write(f"{number} {line}")


main()
