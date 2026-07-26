import sys
import os
import datetime


def create_directory(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)


def create_file(file_1: str) -> None:
    content = []
    while True:
        input_info = input("enter content:")
        if input_info.lower() == "stop":
            break
        content.append(input_info)
    data_now = datetime.datetime.now()
    first_str = data_now.strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_1):
        with open(file_1, "a") as f:
            f.write(f"\n{first_str}\n")
            for num, elem in enumerate(content, start=1):
                f.write(f"{num} {elem}\n")

    else:
        with open(file_1, "w") as f:
            f.write(f"{first_str}\n")
            for num, elem in enumerate(content, start=1):
                f.write(f"{num} {elem}\n")


def main() -> None:
    args = sys.argv[1:]
    dir_parts = []
    name_file = None
    for arg in args:
        if arg == "-d":
            for i in args[args.index(arg) + 1 :]:
                if i != "-f":
                    dir_parts.append(i)
                else:
                    break
        elif arg == "-f":
            name_file = args[args.index(arg) + 1:]
            break

    if dir_parts:
        create_directory(dir_parts)
    if name_file:
        if dir_parts:
            file_path = os.path.join(*dir_parts, name_file[0])
        else:
            file_path = name_file[0]
        create_file(file_path)


if __name__ == "__main__":
    main()
