import os
import sys
import datetime


current_time = datetime.datetime.now()
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


def create_file_structure() -> None:
    args = sys.argv
    current_dir = ""

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1 : f_index]
        else:
            directories = args[d_index + 1 :]

        if directories:
            full_path = os.path.join(*directories)
            os.makedirs(full_path, exist_ok=True)
            current_dir = full_path

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            raise IndexError("You must provide a file name after -f")
        file_name = args[f_index + 1]

        full_file_path = os.path.join(current_dir, file_name)

        with open(full_file_path, "a") as file:
            file.seek(0, 2)
            if file.tell() > 0:
                file.write("\n")
            file.write(f"{current_time}\n")
            page_count = 1
            while True:
                message = input("Enter content line: ")
                if message == "stop":
                    break
                file.write(f"{page_count} {message}\n")
                page_count += 1


if __name__ == "__main__":
    create_file_structure()
