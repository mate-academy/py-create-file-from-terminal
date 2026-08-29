import datetime
import sys
import os


def make_dir(path: str) -> str:
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass

    return path


def make_file(path: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a") as file:
        # check if file not empty
        if os.path.getsize(path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{counter} {line}\n")
            counter += 1


def create_file(*args) -> None:
    # get param list
    param_list = args[0][1:]

    # init default param
    start_index_dir = None
    start_index_file = None

    # get param if exists
    try:
        start_index_dir = param_list.index("-d")
    except ValueError:
        pass
    try:
        start_index_file = param_list.index("-f")
    except ValueError:
        pass

    # if both param empty
    if start_index_dir is None and start_index_file is None:
        return

    # if only dir param exists -> create dirs
    if start_index_dir is not None and start_index_file is None:
        make_dir(os.path.join(*param_list[1:]))
        return

    # if only file param exists -> create file
    if start_index_dir is None and start_index_file is not None:
        make_file(param_list[1])
        return

    # if both exists check it order
    if start_index_dir < start_index_file:
        dir_path = param_list[1:param_list.index("-f")]
        file_path = param_list[param_list.index("-f") + 1:]
    else:
        file_path = param_list[1:param_list.index("-d")]
        dir_path = param_list[param_list.index("-d") + 1:]

    # create path + create dirs
    path = os.path.join(
        make_dir(
            os.path.join(
                *dir_path)
        ),
        file_path[0]
    )

    # create file
    make_file(path)


create_file(sys.argv)
