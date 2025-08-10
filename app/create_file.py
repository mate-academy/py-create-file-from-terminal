from datetime import datetime
from os import makedirs, path
from sys import argv


def create_file():
    directories = []
    file_name = ""

    try:
        ind = argv.index("-d") + 1
    except ValueError:
        pass
    else:
        while ind < len(argv) and argv[ind] != "-f":
            directories.append(argv[ind])
            ind += 1
    finally:
        try:
            file_name = argv[argv.index("-f") + 1]
        except ValueError:
            pass

    if directories:
        makedirs("/".join(directories))

    if file_name:
        full_path = path.join("/".join(directories), file_name)

        if path.exists(full_path):
            file = open(full_path, "a")
            file.write('\n\n')
        else:
            file = open(full_path, "w")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
        inputted_list = []

        while True:
            inputted = input("Enter content line:")
            if inputted == "stop":
                break
            inputted_list.append(inputted)

        file.write('\n'.join(inputted_list))
        file.close()


if __name__ == "__main__":
    create_file()
