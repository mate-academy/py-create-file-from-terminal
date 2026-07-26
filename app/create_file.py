import datetime
import os
import sys


def create_file_and_content(path_to_func: list[str]) -> None:
    if "-d" in path_to_func and "-f" in path_to_func:
        path_dir = (
            path_to_func[path_to_func.index("-d") + 1:path_to_func.index("-f")]
            or path_to_func[path_to_func.index("-d") + 1:]
        )
        path_file = (
            path_to_func[path_to_func.index("-f") + 1:path_to_func.index("-d")]
            or path_to_func[path_to_func.index("-f") + 1:]
        )
        making_directories(path_dir)
        path = os.path.join(*path_dir, *path_file)
        making_file_and_content(path)
    elif "-d" in path_to_func:
        path_dir = path_to_func[path_to_func.index("-d") + 1:]
        making_directories(path_dir)
    else:
        path_file = path_to_func[path_to_func.index("-f") + 1:]
        making_file_and_content(*path_file)


def making_directories(path: list[str]) -> None:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)


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
