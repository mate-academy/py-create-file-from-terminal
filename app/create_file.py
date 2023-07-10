import os
from datetime import datetime


inform = str(input())
inform = inform.strip().split()


def create_a_dir(name_of_dir: str) -> str:
    parent_fod = ""
    for name_of_d in name_of_dir:
        dir_path = os.path.join(parent_fod, name_of_d)
        os.makedirs(dir_path)
        parent_fod = dir_path
    return dir_path


def create_a_file(result_of_dir: str) -> None:
    file_path = os.path.join(result_of_dir, inform[-1])
    with open(file_path, "w") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = date + "\n"
        while True:
            line = str(input("Enter content line: "))
            if line != "stop":
                content += line + "\n"
            else:
                file.write(content)
                break


name_of_dir = []
if inform[0] == "-d":
    for name in inform[1:]:
        if name != "-f":
            name_of_dir.append(name)
        elif name == "-f":
            result_of_dir = create_a_dir(name_of_dir)
            create_a_file(result_of_dir)
            break
    else:
        create_a_dir(name_of_dir)
elif inform[0] == "-f":
    result_of_dir = ""
    create_a_file(result_of_dir)
