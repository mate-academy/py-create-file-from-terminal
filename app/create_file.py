import os
import datetime
import argparse
import io


def write_message(file_to_create: io.TextIOBase) -> None:
    file_to_create.write(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    )
    counter = 1
    while True:
        message = input("Enter content line: ")
        if message == "stop":
            break
        file_to_create.write(f"{counter} {message}\n")
        counter += 1


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", default=[])
    parser.add_argument("-f", nargs=1)
    args = parser.parse_args()

    dir_path = os.path.join(*args.d) if args.d else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if args.f:
        file_name = args.f[0]
        file_path = os.path.join(dir_path, file_name) \
            if dir_path else file_name
        with open(file_path, "a") as file:
            if os.path.getsize(file_path):
                file.write(f"{file_name}\n")
            write_message(file)
    elif not args.d:
        print("Error: You must provide at least -d or -f flag.")


if __name__ == "__main__":
    create_file()
