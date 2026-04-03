from datetime import datetime
import os
import argparse


def main(file_name: str) -> None:
    text = ""
    count = 1

    while True:
        message = input("Enter content line: ")

        if message.lower() == "stop":
            break

        text += f"{count} {message}\n"
        count += 1

    date_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{date_line} \n{text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="file.txt",
        help="file name"
    )
    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        nargs="*",
        default="",
        help="dir name",
    )
    args = parser.parse_args()

    if args.dir:
        directory_path = os.path.join(*args.dir)
        os.makedirs(directory_path, exist_ok=True)
        file_path = os.path.join(directory_path, args.file)
    else:
        file_path = args.file

    main(file_path)
