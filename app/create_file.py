import os
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="*")
parser.add_argument("-f")
args = parser.parse_args()


def update_or_create_file(path: str, command: str) -> None:
    with open(path, command) as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        counter = 1
        while True:
            line = input()
            if line.lower() == "stop":
                f.write("\n")
                break
            f.write(f"{counter} {line}\n")
            counter += 1


if args.d and args.f:
    os.makedirs(os.path.join(*args.d))
    args.d.append(args.f)
    update_or_create_file(os.path.join(*args.d), "w")
elif args.d:
    os.makedirs(os.path.join(*args.d))
elif args.f:
    file_exist: bool = os.path.exists(args.f)
    update_or_create_file(args.f, "a" if file_exist else "w")
