from datetime import datetime
import os
import argparse


def create_file(path: str, filename: str) -> None:
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/{filename}", "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{count} {line_content}\n")
            count += 1
        file.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--dirname",
        nargs="+",
        type=str,
        help="Path to the file"
    )
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        help="Name of the file"
    )
    args = parser.parse_args()

    if args.dirname or args.filename:
        path = "./" + "/".join(args.dirname)
        create_file(path, args.filename if args.filename else "file.txt")
    else:
        print("There are no required arguments. "
              "Must be a dirname or filename argument.")

    print(args)


if __name__ == "__main__":
    main()
