import sys
import os
import datetime


def create_directory(path: list[str]) -> None:
    if path:
        path = os.path.join(*path)
        os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_lines = []
    print("Enter content lines (enter 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        new_lines.append(line.strip())

    with open(file_path, "a") as f:
        f.write(f"{timestamp}\n")
        for index, line in enumerate(new_lines, start=1):
            f.write(f"{index} {line}\n")
        f.write("\n")


def main() -> None:
    qwe = sys.argv[1:]
    if "-d" in qwe and "-f" in qwe:
        dir_index = qwe.index("-d")
        file_index = qwe.index("-f")

        if dir_index > file_index:
            directory_path = qwe[dir_index + 1::]
        else:
            directory_path = qwe[dir_index + 1:file_index]
        file_name = qwe[file_index + 1]

        create_directory(directory_path)
        create_file(os.path.join(*directory_path, file_name))

    elif "-f" in qwe:
        f_index = qwe.index("-f")
        create_file(qwe[f_index + 1])

    elif "-d" in qwe:
        d_index = qwe.index("-d")
        directory_path = qwe[d_index + 1:]
        create_directory(directory_path)
    else:
        raise "Error lol"


if __name__ == "__main__":
    main()
