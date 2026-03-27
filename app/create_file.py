import datetime
import os
import sys


def create_directory(args: list, directory: str) -> str:
    for i in range(args.index("-d"), len(args)):
        if args[i] == "-f":
            break
        directory = os.path.join(directory, args[i])
    os.makedirs(directory)

    return directory


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as f:
        current_time = datetime.datetime.now()
        time_file = current_time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(time_file + "\n")
        count_line = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content != "stop":
                f.write(f"{str(count_line)} {line_content}" + "\n")
                count_line += 1
            else:
                f.write("\n")
                break


def main() -> None:
    args = sys.argv
    directory = os.getcwd()
    if "-d" in args:
        directory = create_directory(args, directory)
    if "-f" in args:
        filename = args[args.index("-f") + 1]
        directory = os.path.join(directory, filename)
        create_file(directory)


if __name__ == "__main__":
    main()
