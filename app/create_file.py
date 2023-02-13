import datetime
import os
import sys


def making_directories(directory_path: list) -> str:
    directory = ""
    if "-d" in directory_path and "-f" not in directory_path:
        for directory_name in directory_path[
            directory_path.index("-d") + 1:
        ]:
            directory += directory_name + "/"
    else:
        for directory_name in directory_path[
            directory_path.index("-d") + 1:
            directory_path.index("-f")
        ]:
            directory += directory_name + "/"
    path_directory = os.path.join(os.getcwd(), directory)
    os.makedirs(path_directory, exist_ok=True)
    return path_directory


def making_file_and_content(directory_path: list) -> None:
    file_path = ""
    if "-d" in directory_path:
        file_path += making_directories(directory_path)

    if "-f" in directory_path:
        file_path += directory_path[directory_path.index("-f") + 1]
        with open(file_path, "a") as file_name:
            file_name.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )

            line_counter = 0
            while True:
                text = input("Enter new line of content: ")
                line_counter += 1
                if text == "stop":
                    break
                file_name.write(f"{line_counter} {text}" + "\n")
            file_name.write("\n")


if __name__ == "__main__":
    directory_path = sys.argv
    making_file_and_content(directory_path)
