import datetime
import sys
import os


def create_file() -> None:
    path = ""
    filename = ""
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        path = os.path.join(
            *args[d_index + 1:args.index("-f")]
            if "-f" in args
            else args[d_index + 1:]
        )
        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]

    file_path = os.path.join(path, filename) if path else filename

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(f"\n{timestamp}\n")
            line_number = sum(1 for _ in open(file_path)) + 1
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1
    else:
        with open(file_path, "w") as file:
            file.write(f"{timestamp}\n")
            line_number = 1
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1

    print(f"File created at: {file_path}")


if __name__ == "__main__":
    create_file()
