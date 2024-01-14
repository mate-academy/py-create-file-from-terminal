import os
import datetime
import sys


def make_dir(path: list[str] | str) -> None:
    pathname = os.path.join(sys.path[0], *path)
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    os.chdir(pathname)


def main() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
    else:
        d_index = False
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
    else:
        f_index = False
    if not f_index and not d_index:
        print("Please use key or keys '-d' - directory path, '-f' - filename")
        return None
    if d_index < f_index:
        make_dir(sys.argv[d_index + 1:f_index])
    else:
        make_dir(sys.argv[d_index + 1:])
        if not f_index:
            return None
    if f_index + 1 == len(sys.argv) or sys.argv[f_index + 1] == "-d":
        print("Wrong filename")
        return None
    write_file(sys.argv[f_index + 1])


def write_file(filename: str) -> None:
    if os.path.exists(filename):
        write_mode = "a"
    else:
        write_mode = "w"
    with open(filename, write_mode) as file:
        file.write(datetime.datetime.now().strftime("%G-%m-%d %H:%M:%S")
                   + "\n")
        line_count = 1
        while True:
            user_input = input("Enter content line:")
            if user_input == "stop":
                break
            file.write(f"{line_count} {user_input}\n")
            line_count += 1
        file.write("\n")


if __name__ == "__main__":
    main()

a = [576, 675765, 76587]
