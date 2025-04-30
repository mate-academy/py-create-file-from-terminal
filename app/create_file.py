import sys
import os
import datetime


def make_directory_or_file() -> None:
    args = sys.argv

    if "-f" not in args and "-d" not in args:
        print("Missing required arguments. Use -f or -d.")
        print("Usage examples:")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    full_dir_path = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if d_index + 1 >= f_index:
                print("No directory names provided after -d.")
                sys.exit(1)
            component_path = args[d_index + 1 : f_index]
        else:
            if d_index + 1 >= len(args):
                print("No directory names provided after -d.")
                sys.exit(1)
            component_path = args[d_index + 1 :]

        full_dir_path = os.path.join(*component_path)
        os.makedirs(full_dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args) or args[f_index + 1].startswith("-"):
            print("Missing file name after -f.")
            sys.exit(1)

        file_name = args[f_index + 1]
        file_path = (
            os.path.join(full_dir_path, file_name)
            if full_dir_path else file_name
        )

        with open(file_path, "a") as f:
            f.write(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + "\n")
            counter = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                f.write(f"{counter} {text}\n")
                counter += 1
