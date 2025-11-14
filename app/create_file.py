import datetime
import sys
import os


def create_path(args: list) -> str | None:
    if "-d" in args:
        index_d = args.index("-d")
        if "-f" in args:
            index_f = args.index("-f")
            dirs = args[index_d + 1:index_f]
        else:
            dirs = args[index_d + 1:]
        return os.path.join(*dirs)
    return None


def create_file(args: list) -> None:
    path = create_path(args)

    if path:
        os.makedirs(path, exist_ok=True)

    if "-f" not in args:
        if path:
            print(f"Directory '{path}' created. No file specified.")
        return

    index_f = args.index("-f")
    if index_f + 1 >= len(args):
        raise ValueError("No file name specified after -f")
    file_name = args[index_f + 1]

    full_path = os.path.join(path, file_name) if path else file_name

    add_blank_line = (os.path.exists(full_path)
                      and os.path.getsize(full_path) > 0)

    with open(full_path, "a") as new_file:
        if add_blank_line:
            new_file.write("\n")
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{time_now}\n")

        counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            new_file.write(f"{counter} {line}\n")
            counter += 1


if __name__ == "__main__":
    create_file(sys.argv)
