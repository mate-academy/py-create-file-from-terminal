import sys
import os
import datetime


def start_path(arg: str, mark: str) -> None:
    with open(arg, mark) as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = input("Enter content line: ")
        line = "1 " + line + "\n"
        i = 1
        while "stop" not in line:
            f.write(line)
            i += 1
            line = input("Enter content line: ")
            line = f"{i} " + line + "\n"
        f.write("\n")


def main() -> None:
    try:
        if sys.argv[1] == "-d":
            if "-f" not in sys.argv:
                path = os.path.join(*sys.argv[2:])
            else:
                index_of_f = sys.argv.index("-f")
                path = os.path.join(*sys.argv[2:index_of_f])
                os.makedirs(path, exist_ok=True)
                start_path(f"{path}/{sys.argv[index_of_f + 1]}", "a")
            os.makedirs(path, exist_ok=True)
        elif sys.argv[1] == "-f":
            start_path(sys.argv[2], "a")
        else:
            print("argv[1] must be either -d or -f!!!")
    except IndexError as e:
        print(f"Not much arguments in sys.argv!!! {e}")


if __name__ == "__main__":
    main()
