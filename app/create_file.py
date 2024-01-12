import os
import sys
import datetime


def name_of_file(args: list) -> str:
    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        args.remove("-f")
        args.remove(file_name)
        return file_name
    return ""


def path_of_file(args: list) -> str:
    if "-d" in args:
        file_name = name_of_file(args)
        args = args[args.index("-d") + 1:]
        path = os.path.join(*args)
        os.makedirs(path, exist_ok=True)
        return os.path.join(*args, file_name)
    return ""


def write_file() -> None:
    args = sys.argv[1:]
    file_path = path_of_file(args)

    with open(file_path, "w") as file:
        counter = 1
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\n")
        input_text = input("Enter content line: ")
        while input_text != "stop":
            file.write(str(counter) + " " + input_text + "\n")
            input_text = input("Enter content line: ")
            counter += 1


if __name__ == "__main__":
    write_file()
