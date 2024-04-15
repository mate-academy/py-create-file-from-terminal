import os
import sys
import datetime


def create_file(filename: str) -> None:
    with open(filename, "w"):
        pass


def main() -> None:
    if len(sys.argv) >= 3:
        if sys.argv[1] == "-d":
            directory_path = os.path.join(*sys.argv[2:])
            print(directory_path)
            os.makedirs(directory_path, exist_ok=True)
        if sys.argv[1] == "-f":
            filename = sys.argv[2]
            create_file(filename)
            with open(filename, "a") as f:
                f.write(datetime.datetime.now().
                        strftime("%Y-%m-%d %H:%M:%S") + "\n")
                while True:
                    count = 0
                    terminal_line = input("Enter content line:")
                    count += 1
                    f.write(str(count) + " " + terminal_line + "\n")
                    if terminal_line.lower() == "stop":
                        break


if __name__ == "__main__":
    main()
