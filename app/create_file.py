import sys
import os
from datetime import datetime


def write_content_to_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def get_args_after_flag(
        flag: str,
        argv: list[str],
        stop_flags: list[str]
) -> list[str]:
    idx = argv.index(flag) + 1
    args = []
    while idx < len(argv):
        if argv[idx].startswith("-") and argv[idx] in stop_flags:
            break
        args.append(argv[idx])
        idx += 1
    return args


if "-d" in sys.argv and "-f" in sys.argv:
    dirs = get_args_after_flag("-d", sys.argv, ["-f"])
    if not dirs:
        print("No directories were provided after the -d flag.")
        sys.exit(1)
    file_name = get_args_after_flag("-f", sys.argv, ["-d"])[0]
    if not file_name:
        print("No file name provided after the -f flag.")
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, file_name)
    write_content_to_file(file_path)

elif "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    dirs = sys.argv[d_index + 1:]
    path = os.path.join(*dirs)
    if dirs:
        os.makedirs(path, exist_ok=True)

elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    if len(sys.argv) > f_index + 1:
        file_name = sys.argv[f_index + 1]
        write_content_to_file(file_name)
    else:
        print("No file name provided after the -f flag.")

else:
    print("Please provide the -d (directories), -f (file), or both flags.")
