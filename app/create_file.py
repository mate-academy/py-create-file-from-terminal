import sys
from datetime import datetime
import os

path = "/Users/trickster/projects/tests/"
now = datetime.now()

dir_path = path

if "-d" in sys.argv:
    index1 = sys.argv.index("-d")
    index2 = sys.argv.index("-f")
    folders = sys.argv[index1 + 1: index2]
    dir_path = os.path.join(path, *folders)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in sys.argv:
    index2 = sys.argv.index("-f")
    filename = sys.argv[index2 + 1]
    file_path = os.path.join(dir_path, filename)

    try:
        with open(file_path, "wt+") as f:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            while True:
                info = input("Enter content line: ")
                if info.lower() == "stop":
                    break
                f.write(f"{info}\n")
    except EOFError:
        pass
