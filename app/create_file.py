import sys
import datetime
import os


def parse_arguments() -> tuple[str, str]:
    arguments = sys.argv
    dir_path = ""
    file_name = ""

    if "-d" in arguments:
        flag_d = arguments.index("-d")
        next_flag = arguments.index("-f") \
            if "-f" in arguments \
            else len(arguments)
        dir_parts = arguments[flag_d + 1:next_flag]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in arguments:
        flag_f = arguments.index("-f")
        file_name = arguments[flag_f + 1]

    return dir_path, file_name


def build_file_path(dir_path: str, file_name: str) -> str:
    return os.path.join(dir_path, file_name) if dir_path else file_name


def write_to_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        print("For stop input please write stop")
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_str}\n")
        count = 1
        while True:
            line = input("Print your message: ")
            if line.lower() == "stop":
                break
            file.write(f"{count} {line}\n")
            count += 1
        file.write("\n")


def main() -> None:
    dir_path, file_name = parse_arguments()
    if not file_name:
        print("Dir created")
    else:
        file_path = build_file_path(dir_path, file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    main()
