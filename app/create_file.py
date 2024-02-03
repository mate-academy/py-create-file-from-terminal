import argparse
import os
from datetime import datetime


def get_content() -> list[str]:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_number = 0
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(f"{line_number} {line}")

    return content


def main() -> None:
    parser = argparse.ArgumentParser(description="Write content to file.")
    parser.add_argument("-d", help="Directory to save the file.", nargs="+")
    parser.add_argument("-f", help="File name to save content.")

    args = parser.parse_args()

    if args.d:
        os.makedirs(os.path.join(*args.d), exist_ok=True)

    if args.f:
        file_path = os.path.join(*args.d, args.f) if args.d else args.f
        with open(file_path, "a") as f:
            content = get_content()
            f.write("\n".join(content))
            f.write("\n\n")


if __name__ == "__main__":
    main()
