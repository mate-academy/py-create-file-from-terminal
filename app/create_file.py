import sys
import datetime
import os


dataset = sys.argv[1:]
path = None
file_name = None
if "-d" in dataset:
    dataset.remove("-d")
    if "-f" not in dataset:
        path = os.path.join(*dataset)
    else:
        path = os.path.join(*dataset[0: dataset.index("-f")])
    file_name = dataset[-1] if "-f" in dataset else None
if path:
    os.makedirs(path, exist_ok=True)
if file_name:
    if path:
        os.chdir(path)
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        file.write(
            datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        content_line = input("Enter content line:")
        iteration = 0
        while content_line != "stop":
            iteration += 1
            file.write(f"{iteration} {content_line} \n")
            content_line = input("Enter content line:")
        file.write("\n")
