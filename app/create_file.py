from sys import argv
from os import makedirs, path
from datetime import datetime


def main() -> None:
    argument_list = argv[1:]
    file_name = ""
    current_path = ""

    if "-f" in argv:
        file_name = argument_list.pop(argument_list.index("-f") + 1)
        argument_list.remove("-f")

    if "-d" in argument_list:
        argument_list.remove("-d")
        current_path = path.join(*argument_list)
        makedirs(current_path, exist_ok=True)

    if file_name:
        create_file_with_content(str(path.join(current_path, file_name)))


def create_file_with_content(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_num = 1
        while True:
            input_content = input("Enter content line:")
            if input_content == "stop":
                file.write("\n")
                break

            file.write(f"{line_num} {input_content}\n")
            line_num += 1


if __name__ == "__main__":
    main()
