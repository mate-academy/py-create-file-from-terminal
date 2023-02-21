import argparse
import time
import os


parser = argparse.ArgumentParser()
parser.add_argument("-d", type=str, nargs="*")
parser.add_argument("-f", type=str)
args = parser.parse_args()


def create_update_file(f_path: str, mode: str) -> None:
    with open(f_path, mode) as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        line_num = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                f.write("\n")
                break
            f.write(f"{line_num} {content_line}\n")
            line_num += 1


if __name__ == "__main__":
    if args.d and args.f:
        os.makedirs(os.path.join(*args.d), exist_ok=True)
        file_path = os.path.join(*args.d, str(args.f))
        file_exist: bool = os.path.exists(file_path)
        create_update_file(file_path, "a" if file_exist else "w")
    elif args.d:
        os.makedirs(os.path.join(*args.d), exist_ok=True)
    else:
        file_path = os.path.join(args.f)
        file_exist: bool = os.path.exists(file_path)
        create_update_file(file_path, "a" if file_exist else "w")
