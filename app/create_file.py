import sys
import os
import datetime


for arg in sys.argv:
    if arg == "-d":
        if "-f" not in sys.argv:
            target_path = os.path.join("/".join(sys.argv[2:]))
        else:
            target_path = os.path.join("/".join(sys.argv[2:-2]))
        if not os.path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
        os.chdir(target_path)

filename = sys.argv[-1] if "-f" in sys.argv else "file.txt"

with open(filename, "a") as file:
    current_date = datetime.datetime.now()
    file.write(current_date.strftime("%Y-%d-%m %H:%M:%S") + "\n")
    while True:
        content = input("Enter content line: ")
        count = 1
        if content == "stop":
            break
        file.write(f"{count} " + content + "\n")
        count += 1
