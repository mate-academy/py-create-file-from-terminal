import os
import argparse
import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a+") as new_file:
        count_lines = 0
        current_date = datetime.datetime.now()
        new_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S \n"))
        while True:
            input_string = input(
                "Input content lines until you input stop: "
            )
            count_lines += 1
            if input_string == "stop":
                break
            new_file.writelines(f"{count_lines} {input_string}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*")
    parser.add_argument("-f")
    args = parser.parse_args()
    path = os.path.join(os.getcwd(), "app")
    if args.d:
        directory_path = os.path.join(path, *args.d)
        os.makedirs(directory_path, exist_ok=True)
    if args.f:
        file_path = os.path.join(path, args.f)
        if args.d and args.f:
            file_path = os.path.join(path, *args.d, args.f)

        try:
            create_file(file_path)
        except FileNotFoundError:
            print(f"Cannot open file: {file_path}")
        except PermissionError:
            print(f"You do not have permission to write to file: {file_path}")
