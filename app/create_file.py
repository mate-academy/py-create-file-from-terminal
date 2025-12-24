import sys
import os
import datetime


def create_dir(current_dir: str, list_parts_dir: list[str]) -> str:
    directory_path = os.path.join(current_dir, *list_parts_dir)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(current_dir: str, name_file: str) -> None:
    file_path = os.path.join(current_dir, name_file)

    with open(f"{file_path}", "a") as f:
        current_time = datetime.datetime.now()
        f.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        number_line = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            number_line += 1
            f.write(f"{number_line} {line}\n")
        f.write("\n")


def create_file_from_terminal() -> None:

    error_message = (
        "Enter correctly command please:\n"
        "[-d dir1 [dir2..]] for create directory\n"
        "[-f file.txt] for create file \n"
        "[-d dir1 dir2..] [-f file.txt] for create directory "
        "and file in this directory"
    )
    command_length = len(sys.argv)
    index_d = sys.argv.index("-d") if "-d" in sys.argv else 0
    index_f = sys.argv.index("-f") if "-f" in sys.argv else 0
    if (
            (index_f == 0 and index_d == 0)
            or (index_d == index_f + 1 and index_f != 0)
            or (index_f == index_d + 1 and index_d != 0)
    ):
        print(error_message)
    else:
        current_directory = os.path.dirname(sys.argv[0])
        if index_d > 0:
            if index_f == 0 and index_d != command_length - 1:
                create_dir(current_directory, sys.argv[index_d + 1:])
            elif index_d < index_f != command_length - 1:
                new_directory = create_dir(
                    current_directory,
                    sys.argv[index_d + 1:index_f]
                )
                create_file(new_directory, sys.argv[index_f + 1])
            elif index_f < index_d != command_length - 1:
                new_directory = create_dir(
                    current_directory,
                    sys.argv[index_d + 1:])
                create_file(new_directory, sys.argv[index_f + 1])
            else:
                print(error_message)
        elif command_length - 1 != index_f > 0 == index_d:
            create_file(current_directory, sys.argv[index_f + 1])


if __name__ == "__main__":
    create_file_from_terminal()
