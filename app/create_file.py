import sys
import os
import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_to_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        counter = 0
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                file.write("\n")
                break
            counter += 1
            file.write(f"{counter} {content}\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        if d_index < f_index:
            dir_path = os.path.join(*args[d_index + 1:f_index])
            file_name = args[f_index + 1]
        else:
            dir_path = os.path.join(*args[d_index + 1:])
            file_name = args[f_index + 1]
        create_directory(dir_path)
        file_path = os.path.join(dir_path, file_name)
        write_to_file(file_path)
    elif "-d" in args:
        dir_path = os.path.join(*args[args.index("-d") + 1:])
        create_directory(dir_path)
    elif "-f" in args:
        file_name = args[args.index("-f") + 1]
        write_to_file(file_name)
    else:
        print("Invalid arguments. Use -d for directory and/or -f for file.")


if __name__ == "__main__":
    main()
