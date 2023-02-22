import os
import sys
from datetime import datetime

if "-d" in sys.argv:
    dir_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
    os.makedirs(dir_path, exist_ok=True)
else:
    dir_path = "."

if "-f" in sys.argv:
    file_path = os.path.join(dir_path, sys.argv[sys.argv.index("-f") + 1])
    with open(file_path, "a" if os.path.exists(file_path) else "w") as f:
        if f.tell() == 0:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        for i, line in enumerate(iter(input, "stop"), 1):
            f.write(f"{i} {line}\n")
else:
    print("Error: -f flag is missing")
    sys.exit(1)
