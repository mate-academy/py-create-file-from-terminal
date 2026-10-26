import sys
import datetime
import os

path = ""

if "-d" in sys.argv:
    start = sys.argv.index("-d") + 1
    end = len(sys.argv)

    if "-f" in sys.argv and sys.argv.index("-f") > start:
        end = sys.argv.index("-f")

    folders = sys.argv[start:end]

    if folders:
        path = os.path.join(*folders)
        os.makedirs(path, exist_ok=True)

if "-f" in sys.argv:
    filename = sys.argv[sys.argv.index("-f") + 1]
    filename = os.path.join(path, filename)

    with open(filename, "a") as file:
        if file.tell() > 0:
            file.write("\n")

        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time + "\n")

        number = 1

        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{number} {content}\n")
            number += 1
