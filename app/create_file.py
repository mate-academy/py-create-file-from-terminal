import sys
import os
import datetime


def write_into_file(path: str) -> None:
    with open(path, "a") as file:
        count_of_lines = 0
        file.write(str(current_day.strptime(
            current_day.strftime("%I:%M%p %d/%B/%Y"),
            "%I:%M%p %d/%B/%Y")) + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            else:
                file.write(str(count_of_lines) + " " + line + "\n")
                count_of_lines += 1


def make_dirs(path: str) -> None:
    os.makedirs(path)


current_day = datetime.datetime.now()
if "-d" in sys.argv and "-f" not in sys.argv:
    path = os.path.join(*sys.argv[sys.argv.index("-d") + 1: len(sys.argv)])
    make_dirs(os.path.join("app", path))
elif "-f" in sys.argv and "-d" not in sys.argv:
    write_into_file(os.path.join("app", sys.argv[sys.argv.index("-f") + 1]))
else:
    if sys.argv.index("-d") == 1:
        path = sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        dirs_path = os.path.join(*path)

    else:
        dirs_path = os.path.join(*(sys.argv[sys.argv.index("-d") + 1:
                                            len(sys.argv)]))
    whole_path = os.path.join(dirs_path, sys.argv[sys.argv.index("-f") + 1])
    make_dirs(os.path.join("app", dirs_path))
    write_into_file(os.path.join("app", whole_path))
