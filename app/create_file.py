import os
import sys
import datetime


def get_directory_names() -> list:
    dir_names = []
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        if d_index < len(sys.argv) - 1:
            i = d_index + 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                dir_names.extend(sys.argv[i].split(","))
                i += 1
    return dir_names


def get_file_name() -> str:
    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        if f_index < len(sys.argv) - 1:
            file_name = sys.argv[f_index + 1]
    return file_name


def create_directories(dir_names: list) -> None:
    nested_dir = ""
    for dir_name in dir_names:
        nested_dir = os.path.join(nested_dir, dir_name)
        os.makedirs(nested_dir, exist_ok=True)


def create_file(file_name: str, dir_names: list) -> None:
    if file_name and not file_name.startswith("-") and dir_names:
        nested_dir = os.path.join(*dir_names)
        file_path = os.path.join(nested_dir, file_name)
        with open(file_path, "w") as f:
            # Adding date and time to the file
            now = datetime.datetime.now()
            f.write(f"Creation time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            # Inputting file content
            print(f"Enter content for {file_path} "
                  f"(press Enter on an empty line to finish):")
            content = ""
            while True:
                line = input()
                if line == "stop":
                    break
                content += line + "\n"
            f.write(content)
            f.write("\n")


def main() -> None:
    dir_names = get_directory_names()
    file_name = get_file_name()
    create_directories(dir_names)
    create_file(file_name, dir_names)


if __name__ == "__main__":
    main()
