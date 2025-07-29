from sys import argv
from os import makedirs, path
from datetime import datetime

name = argv[1:]


def with_d(road: list) -> None:
    dirs = path.join(*road)
    makedirs(dirs)


def with_f(file_name: str) -> None:
    with open(file_name, "a") as doc:
        text = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            text.append(line)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        doc.write(now + "\n")
        for number in range(len(text)):
            doc.write(f"{number + 1} {text[number]}\n")


if "-d" in name and "-f" in name:
    road_for_dic = name[name.index("-d") + 1 : name.index("-f")]
    file_name = name[name.index("-f") + 1]
    with_d(road_for_dic)
    file_path = path.join(*road_for_dic, file_name)
    with_f(file_path)


elif "-d" in name:
    road_for_dic = name[name.index("-d") + 1 :]
    with_d(road_for_dic)
elif "-f" in name:
    file_name = name[name.index("-f") + 1]
    with_f(file_name)
