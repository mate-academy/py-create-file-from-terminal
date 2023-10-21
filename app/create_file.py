import argparse
import os
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()
    if args.d:
        os.makedirs(os.path.join(*args.d), exist_ok=True)
        os.chdir(os.path.join(*args.d))
    if args.f:
        with open(args.f, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            print("Enter content or 'stop'")
            for counter, line in enumerate(iter(input, "stop")):
                print(f"{counter + 1} {line}\n")


if __name__ == "__main__":
    main()
