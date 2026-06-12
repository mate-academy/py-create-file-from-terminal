import datetime
import os
import sys


def parse_arguments() -> tuple[list[str], str | None]:
    d_name = []
    f_name = None

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        f_name = sys.argv[f_index + 1]

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        if "-f" in sys.argv and sys.argv.index("-f") > d_index:
            d_name = sys.argv[d_index + 1: sys.argv.index("-f")]
        else:
            d_name = sys.argv[d_index + 1:]

    return d_name, f_name


def create_file_and_content(file_path: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:

        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")
        line_number = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input.lower().strip() == "stop":
                break

            file.write(f"{line_number} {user_input}\n")
            line_number += 1


def main() -> None:
    d_name, f_name = parse_arguments()

    if d_name:

        directory_path = os.path.join(*d_name)
        os.makedirs(directory_path, exist_ok=True)

        if f_name:
            full_path = os.path.join(directory_path, f_name)
            create_file_and_content(full_path)
    else:
        if f_name:
            create_file_and_content(f_name)


if __name__ == "__main__":
    main()
