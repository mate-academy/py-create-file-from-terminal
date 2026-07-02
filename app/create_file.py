import argparse
import datetime
import os


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", default=None)
    parser.add_argument("-f", default=None)

    args = parser.parse_args()

    directory = ""
    if args.d:
        directory = os.path.join(*args.d)
        os.makedirs(directory, exist_ok=True)

    if args.f is None:
        return

    file_path = os.path.join(directory, args.f)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(
            datetime.datetime.now().
            strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


if __name__ == "__main__":
    main()
