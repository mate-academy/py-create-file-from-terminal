import os
from datetime import datetime
import sys


def main() -> None:
    cmd_string = sys.argv[1:]
    cur_dir = os.getcwd()

    if "-d" in cmd_string:
        d_indx = cmd_string.index("-d")
        cmd_path = []
        d_indx += 1
        while (d_indx < len(cmd_string)
               and
               not cmd_string[d_indx].startswith("-")):
            cmd_path.append(cmd_string[d_indx])
            d_indx += 1
        cur_dir = os.path.join(cur_dir, *cmd_path)
        os.makedirs(cur_dir, exist_ok=True)

    if "-f" in cmd_string:
        f_indx = cmd_string.index("-f")
        try:
            f_name = cmd_string[f_indx + 1]
        except IndexError:
            print("The file name is absent after -f")
        else:
            f_path = os.path.join(cur_dir, f_name)
            try:
                with open(f_path, "a") as f:
                    f.write(datetime.now().strftime("%Y-%M-%D %H:%M:%S")
                            + "\n")
                    line = 1
                    text = input("Enter content line: ")
                    while text.lower() != "stop":
                        f.write(f"{line} {text}\n")
                        line += 1
                        text = input("Enter content line: ")
                    f.write("\n")
            except OSError:
                print("Unexpected file name after -f")


if __name__ == "__main__":
    main()
