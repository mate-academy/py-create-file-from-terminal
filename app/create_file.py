from datetime import datetime
from sys import argv
import os


def create_dir_or_file(dir_l: list, file_l: list) -> None:
    dir_str = os.path.join("app", *dir_l[1:])
    os.makedirs(dir_str) if dir_l[1:] else None

    if file_l:
        with open(os.path.join(dir_str, *file_l[1:]), "a") as f:
            f.writelines(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            count = 1
            text = input("Enter content line: ")
            while text.lower() != "stop":
                f.writelines(f"\n{str(count)} {text}")
                count += 1
                text = input("Enter content line: ")


def read_flag() -> None:
    flag_d = []
    flag_f = []
    index = {"-d": -1, "-f": -1}
    for i in index:
        try:
            index[i] = argv.index(i)
        except ValueError:
            continue

    if len(argv) <= 1 or all(x == -1 for x in index.values()):
        raise Exception("Missing any flags")

    if index["-f"] > index["-d"] > -1:
        flag_d = argv[index["-d"]:index["-f"]]
    elif index["-f"] < index["-d"]:
        flag_d = argv[index["-d"]:]

    if index["-d"] < index["-f"]:
        flag_f = argv[index["-f"]:]

    create_dir_or_file(flag_d, flag_f)


if __name__ == "__main__":
    read_flag()
