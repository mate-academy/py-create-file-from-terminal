import argparse
import datetime
import os


def create_file(path: str) -> None:
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exist = os.path.exists(path) and os.path.getsize(path) > 0
    with open(path, "a") as current_file:
        if exist:
            current_file.write("\n")
        current_file.write(current_date + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            current_file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file")

    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    if args.d and not args.f:
        build_dir = os.path.join(*args.d)
        os.makedirs(build_dir, exist_ok=True)

    elif args.f and not args.d:
        path = args.f
        create_file(path)

    elif args.d and args.f:
        build_dir = os.path.join(*args.d)
        os.makedirs(build_dir, exist_ok=True)
        path = os.path.join(build_dir, args.f)
        create_file(path)
    else:
        parser.error("Please provide -d or -f")


if __name__ == "__main__":
    main()
