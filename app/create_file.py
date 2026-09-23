import sys
import os
from datetime import datetime


def main() -> None:
    if len(sys.argv) < 3:
        print("Error")
        return None
    dir_list = []
    for element in range(len(sys.argv)):
        if sys.argv[element] == "-d":
            for direct in range(element + 1, len(sys.argv)):
                if sys.argv[direct] == "-f":
                    break
                dir_list.append(sys.argv[direct])
    result_dir = "/".join(dir_list)
    file_name = sys.argv[-1]
    now = datetime.now()
    timestamp = now.strftime("%d.%m.%Y %H:%M:%S")
    if "-d" in sys.argv:
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
            print("Folder created!")
        else:
            print("That folder already exists")
    if "-f" in sys.argv:
        parent_dir = os.path.dirname(result_dir)
        if parent_dir and not os.path.exists(result_dir):
            os.makedirs(result_dir)
        if os.path.exists(result_dir):
            with open(f"./{result_dir}/{file_name}.txt",
                      "a", encoding="utf-8") as f:
                line = 1
                f.write(f"{timestamp}\n")
                while True:
                    content = input("Enter content line: ")
                    if content.lower() == "stop":
                        return None
                    f.write(f"{line} {content}\n")
                    line += 1

        with open(f"./{result_dir}/{file_name}.txt",
                  "w", encoding="utf-8") as f:
            line = 1
            f.write(f"{timestamp}\n")
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                f.write(f"{line} {content}\n")
                line += 1
    else:
        print("Unexist command!")
