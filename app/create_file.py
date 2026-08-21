import os
import sys
from datetime import datetime


def arg_processing(sys_argv: list[str]) -> dict[str, str | None]:
    args = sys_argv[1:]
    dirs = []
    filename = None
    result_dict: dict[str, str | None] = {
        "dir_path": None,
        "filename": None,
        "flags": "N"
    }

    if "-d" in args and "-f" in args:
        index_d = args.index("-d")
        index_f = args.index("-f")
        if index_d < index_f:
            dirs = args[index_d + 1:index_f]
            filename = args[index_f + 1]
        else:
            filename = args[index_f + 1]
            dirs = args[index_d + 1:]

        result_dict["dir_path"] = str(os.path.join(*dirs)) if dirs else None
        result_dict["filename"] = filename
        result_dict["flags"] = "f+d"
    elif "-f" in args:
        index_f = args.index("-f")
        filename = args[index_f + 1]
        result_dict["filename"] = filename
        result_dict["flags"] = "f"
    elif "-d" in args:
        index_d = args.index("-d")
        dirs = args[index_d + 1:]
        result_dict["dir_path"] = str(os.path.join(*dirs)) if dirs else None
        result_dict["flags"] = "d"

    return result_dict


def create_file(filepath: str) -> None:
    list_result = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line = input("Enter content line: ")
    if line != "stop":
        list_result.append(line)
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            list_result.append(line)

    if len(list_result) > 1:
        file_exists = os.path.exists(filepath)
        with open(filepath, "a") as f:
            if file_exists:
                f.write("\n")

            f.write(f"{list_result[0]}\n")
            for i, item in enumerate(list_result[1:], start=1):
                f.write(f"{i} {item}\n")


dirs_and_filename_dict = arg_processing(sys.argv)
if dirs_and_filename_dict["flags"] == "f+d":
    os.makedirs(str(dirs_and_filename_dict["dir_path"]), exist_ok=True)
    path = os.path.join(
        str(dirs_and_filename_dict["dir_path"]),
        str(dirs_and_filename_dict["filename"])
    )
    create_file(path)
elif dirs_and_filename_dict["flags"] == "d":
    path = str(dirs_and_filename_dict["dir_path"])
    os.makedirs(str(dirs_and_filename_dict["dir_path"]), exist_ok=True)
elif dirs_and_filename_dict["flags"] == "f":
    path = str(dirs_and_filename_dict["filename"])
    create_file(path)
