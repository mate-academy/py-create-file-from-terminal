import datetime
import os
import sys


def main():
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        directories_name = get_directories(args)
        filename = get_filename(args)
        full_path = os.path.join(directories_name, filename)
        lines = get_content()
        write_to_file(full_path, lines)
    elif "-d" in args:
        get_directories(args)
    elif "-f" in args:
        filename = get_filename(args)
        lines = get_content()
        write_to_file(filename, lines)



def get_directories(args):
    if "-d" in args:
        if "-f" in args:
            only_d = sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        else:
            only_d = sys.argv[sys.argv.index("-d") + 1:]
        path = os.path.join(*only_d)
        os.makedirs(path, exist_ok=True)
        return path
    return None

def get_filename(args):
    if "-f" in args:
        only_f = sys.argv[sys.argv.index("-f") + 1]
        return only_f
    return None

def write_to_file(file_path, lines):
    with open(file_path, "a") as file_assertion:
        file_assertion.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for index, line in enumerate(lines, 1):
            file_assertion.write(f"{index} {line}\n")

def get_content():
    lines = []
    line = input("Enter content line: ")
    while line != "stop":
        lines.append(line)
        line = input("Enter content line: ")
    return lines

if __name__ == "__main__":
    main()
