import sys
import os
import datetime


arguments = sys.argv
path = ""
if "-d" in arguments:
    directories = [arg for arg in arguments if "dir" in arg]
    path = "/".join(directories)
    if not os.path.isdir(path):
        os.makedirs(path)
    path += "/"
if "-f" in arguments:
    text = ""
    count = 1
    while True:
        answer = input("Enter content line:")
        if answer == "stop":
            break
        text += f"{count} {answer}\n"
        count += 1
    with open(f"{path}{arguments[-1]}", "a") as file:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time}\n{text}")
        file.write("\n")
