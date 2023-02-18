import datetime
import os
import sys


def create_file_and_content(path_to_func: str) -> None:
    if "-f" in path_to_func and "-d" in path_to_func:
        if path_to_func.index("-d") > path_to_func.index("-f"):
            flag_f = (
                path_to_func[path_to_func.index("-f"):path_to_func.index("-d")]
            )
            flag_d = path_to_func[path_to_func.index("-d"):]
            path_to_func_replaced = flag_d + flag_f
            path = path_to_func_replaced[
                path_to_func_replaced.index("-d") + 1:
                path_to_func_replaced.index("-f")
            ]
            path = (
                making_directories(path) + "/"
                + path_to_func_replaced[path_to_func_replaced.index("-f") + 1]
            )
            making_file_and_content(path)

        else:
            path = path_to_func[
                path_to_func.index("-d") + 1: path_to_func.index("-f")
            ]
            path = (
                making_directories(path) + "/"
                + path_to_func[path_to_func.index("-f") + 1]
            )
            making_file_and_content(path)
    elif "-f" in path_to_func and "-d" not in path_to_func:
        path = path_to_func[path_to_func.index("-f") + 1]
        making_file_and_content(path)
    elif "-d" in path_to_func and "-f" not in path_to_func:
        path = path_to_func[path_to_func.index("-d") + 1:]
        making_directories(path)


def making_directories(path: str) -> str:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)
    return path


def making_file_and_content(path: str) -> None:
    with open(path, "a") as file_name:
        file_name.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        line_counter = 0
        while True:
            text = input("Enter new line of content: ")
            line_counter += 1
            if text == "stop":
                break
            file_name.write(f"{line_counter} {text}\n")
        file_name.write("\n")


if __name__ == "__main__":
    path_to_func = sys.argv
    create_file_and_content(path_to_func)
