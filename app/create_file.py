import argparse
import datetime
import os


def main():
    parser = argparse.ArgumentParser(description='Create file')

    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    if args.d and not args.f:
        build_dir = os.path.join(*args.d)
        os.makedirs(build_dir, exist_ok=True)

    elif args.f and not args.d:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        exist = os.path.exists(args.f) and os.path.getsize(args.f) > 0
        with open(args.f, "a") as file:
            if exist:
                file.write("\n")
            file.write(current_date+ "\n")
            i = 1
            while True:
                    content = input("Enter content line: ")
                    if content == "stop":
                        break
                    file.write(f"{i} {content}\n")
                    i += 1
    elif args.d and args.f:
        build_dir = os.path.join(*args.d)
        os.makedirs(build_dir, exist_ok=True)
        path = os.path.join(build_dir, args.f)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        exist = os.path.exists(path) and os.path.getsize(path) > 0
        with open(path, "a") as file:
            if exist:
                file.write("\n")
            file.write(current_date + "\n")
            i = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file.write(f"{i} {content}\n")
                i += 1
    else:
        parser.error("Please provide -d or -f")


if __name__ == "__main__":
    main()
