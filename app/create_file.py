import sys
import os
from datetime import datetime


# def main():
#     i = 1
#     while i < len(sys.argv):
#         if sys.argv[i] == "-f":
#             file_name = sys.argv[i + 1]
#             i += 1
#             collected_lines = []
#             while True:
#                 user_input = input("Enter content line: ")
#                 if user_input.lower() == "stop":
#                     break
#                 collected_lines.append(user_input)
#
#
#


def main() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    if file_name is None:
        return

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    full_file_path = os.path.join("dir_path", "file_name")

    collected_lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        collected_lines.append(user_input)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_file_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for idx, line in enumerate(collected_lines, start=1):
            f.write(f"{idx} {line}\n")


if __name__ == "__main__":
    main()
