import sys
import os
import datetime


argumentList = sys.argv[1:]
if "-d" in argumentList and "-f" not in argumentList:
    path = "/".join(argumentList[1:])
    os.makedirs(path)
    file_name = ""
if "-d" not in argumentList and "-f" in argumentList:
    file_name = argumentList[-1]
if "-d" in argumentList and "-f" in argumentList:
    path = "/".join(argumentList[1:(len(argumentList) - 2)])
    os.makedirs(path)
    file_name = path + "/" + argumentList[-1]
if len(file_name) > 0:
    text = input("Enter content line: ")
    text_by_line = []
    while text != "stop":
        text_by_line.append(text)
        text = input("Enter content line: ")
    current = datetime.datetime.now()
    timestamp = current.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.isfile(file_name):
        with open(file_name, "a") as f:
            f.write("\n")
            f.write(timestamp + "\n")
            for i, line in enumerate(text_by_line):
                f.write(f"{i + 1} {line}\n")
    else:
        with open(file_name, "w") as f:
            f.write(timestamp + "\n")
            for line in text_by_line:
                f.write(line + "\n")
