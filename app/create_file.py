import datetime
import os
import sys


def parser_simple(key: str) -> str:
    args = sys.argv
    out = ""
    for i, arg in enumerate(args):
        if key in arg:
            out = args[i + 1:]

            for j, new_arg in enumerate(path):
                if "-" in new_arg:
                    out = args[i + 1:i + j + 1]
                    break

    print("Path = ", out)
    return out



def create_argument() -> dict:
    out = {}
    args = sys.argv
    filename = ""
    path = ""
    new_path = ""
    new_filename = ""
    print(args)

    for i, arg in enumerate(args):
        if "-d" in arg:
            path = args[i + 1:]

            for j, new_arg in enumerate(path):
                if "-" in new_arg:
                    path = args[i + 1:i + j + 1]
                    break

    print("Path = ", path)

    # if arg in "-f":
    #     new_args = args[i + 1:]
    #     print("New str f:", new_args)
    #     for j, new_arg in enumerate(new_args):
    #         if "-" in new_arg:
    #             print("Bingo f")
    #             filename = args[i + 1:j]
    #     filename = args[args.index("-f"):]

    new_filename = " ".join(filename[1:])
    new_path = os.path.join("/".join(path[1:]))

    print("File:", filename[1:])
    print(new_filename)
    print("Path:", path[1:])
    print(new_path)

    # if ("-d" in args) and ("-f" in args):
    #     print("Directory and File")
    #     filename = args[args.index("-f"):]
    #     path = args[args.index("-d"):args.index("-f")]
    #
    #     new_filename = " ".join(filename[1:])
    #     new_path = os.path.join("/".join(path[1:]))
    #
    #     print("File:", filename[1:])
    #     print(new_filename)
    #     print("Path:", path[1:])
    #     print(new_path)
    #
    # elif "-d" in args:
    #     print("only Directory")
    #     path = args[args.index("-d"):]
    #     new_path = os.path.join("/".join(path[1:]))
    #     print(new_path)
    # elif "-f" in args:
    #     print("only File")
    #     filename = args[args.index("-f"):]
    #     new_filename = " ".join(filename[1:])
    #     print(new_filename)
    # else:
    #     print("No key")

    if new_path:
        out["path"] = new_path

    if new_filename:
        out["filename"] = new_filename

    return out


# def create_argument_new() -> dict:
#     out = {}
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-d")
#     parser.add_argument("-f")
#     args = parser.parse_args()
#
#     out["path"] = args.d
#     out["filename"] = args.f
#     print(out)
#
#     return out


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

    while input_str != "stop":
        input_str = input("Enter content line:")
        if input_str != "stop":
            buff.append(input_str)

    if not buff:
        return

    # file_name_str = create_dir(input_arg) + input_arg["filename"]
    file_name_str = os.path.join(create_dir(input_arg), input_arg["filename"])

    with open(file_name_str, "at") as file:
        current = datetime.datetime.now()
        file.write(current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, data in enumerate(buff):
            file.write(f"{i + 1} {data}\n")


# create_argument_new()
# # create_file(create_argument())
if __name__ == "__main__":
    create_file(create_argument())
