import datetime
import os
import sys


def main() -> None:
    if len(sys.argv) < 3:
        return

    if sys.argv[1] == "-d" and sys.argv[-2] == "-f":
        path = sys.argv[2:-2]
        new_path = create_path(path)
        filename = os.path.join(new_path, sys.argv[-1])

    elif sys.argv[1] == "-f" and "-d" in sys.argv:
        path_index = sys.argv.index("-d")
        new_path = create_path(sys.argv[path_index + 1:])
        filename = os.path.join(new_path, sys.argv[2])

    elif sys.argv[1] == "-d":
        path = sys.argv[2:]
        create_path(path)
        return

    elif sys.argv[1] == "-f":
        filename = sys.argv[2]

    else:
        return

    with open(filename, "a+") as f:
        counter = 0
        while True:
            content = input("Enter content line: ")
            if not content == "stop":
                if counter == 0:
                    timestamp = datetime.datetime.now(
                    ).strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"{timestamp}\n")
                    counter += 1
                f.write(f"{content}\n")
            else:
                break


def create_path(items: list) -> str:
    curr = os.getcwd()
    new_path = os.path.join(curr, *items)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


if __name__ == "__main__":
    main()
