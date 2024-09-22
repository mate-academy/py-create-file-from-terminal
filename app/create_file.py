import os
import sys
from dir import create_directory
from file import create_file


def creator():
    args = sys.argv

    dir_index = args.index("-d") + 1 if "-d" in args else None
    file_index = args.index("-f") + 1 if "-f" in args else None

    if dir_index and file_index and dir_index < file_index:
        dir_path = args[dir_index:file_index - 1]
        file_name = args[file_index]
        directory = create_directory(dir_path)
        create_file(os.path.join(directory, file_name))
    elif dir_index and not file_index:
        dir_path = args[dir_index:]
        create_directory(dir_path)

    elif not dir_index and file_index:
        file_name = args[file_index]
        create_file(file_name)
    else:
        raise TypeError(
            "You must provide either a directory (-d) "
            "or file (-f) argument."
        )


if __name__ == "__main__":
    creator()
