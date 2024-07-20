import datetime
import os
import sys


def parser_simple(key: str) -> str:
    args = sys.argv
    out = ""
    for index, arg in enumerate(args):
        if key in arg:
            out = args[index + 1:]

            for count, new_arg in enumerate(out):
                if "-" in new_arg:
                    out = args[index + 1:index + count + 1]
                    break

    print("Path = ", out)
    return out


def create_argument() -> dict:
    out = {}

    new_filename = " ".join(parser_simple("-f"))
    new_path = os.path.join("/".join(parser_simple("-d")))

    if new_path:
        out["path"] = new_path

    if new_filename:
        out["filename"] = new_filename

    return out


def create_dir(input_arg: dict) -> str:
    if "path" in input_arg:
        path = os.path.join(input_arg["path"])
        print("Path:", path)
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    return ""


def create_file(input_arg: dict) -> None:
    create_dir(input_arg)
    if "filename" not in input_arg:
        return

    input_str = ""
    buff = []
    file_name_str = os.path.join(create_dir(input_arg), input_arg["filename"])

    while input_str != "stop":
        input_str = input("Enter content line:")
        if input_str != "stop":
            buff.append(input_str)


    if not buff:
        return


    with open(file_name_str, "at") as file:
        current = datetime.datetime.now()
        file.write(current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, data in enumerate(buff):
            file.write(f"{i + 1} {data}\n")


if __name__ == "__main__":
    create_file(create_argument())
