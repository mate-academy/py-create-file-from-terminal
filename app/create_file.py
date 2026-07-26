from datetime import datetime
from sys import argv
from os import mkdir


def check_flags():
    try:
        if "-d" in argv and "-f" in argv:
            return "fd"
        if "-f" in argv:
            return "f"
        elif "-d" in argv:
            return "d"
        else:
            raise Exception
    except Exception:
        raise Exception('Called without flag/flags')


def content():
    input_content = []

    while True:
        line = input("Enter content line: ")
        if line != "stop":
            input_content.append(line + "\n")
        else:
            break

    return input_content


def write_to_file(file_path):
    with open(file=file_path, mode='a') as file_out:
        input_content = content()
        file_out.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        file_out.writelines(input_content)


def create_directory(dir_names):
    counter = 0
    path_to_file = str(dir_names[counter])

    while True:
        try:
            mkdir(path_to_file)
        except (FileNotFoundError, FileExistsError):
            counter += 1
            if counter < len(dir_names):
                path_to_file += '/' + str(dir_names[counter])
                continue
            else:
                break


def create_path():
    flags = check_flags()
    if flags == "f":
        file_index = argv.index("-f")
        file_path = '/'.join(argv[file_index + 1:])
        return file_path
    elif flags == "d":
        dir_index = argv.index("-d")
        file_path = '/'.join(argv[dir_index + 1:])
        return file_path
    elif flags == "fd":
        dir_index = argv.index("-d")
        file_index = argv.index("-f")
        file_path = '/'.join(
            argv[dir_index + 1:file_index] + argv[file_index + 1:]
        )
        return file_path


def create_file():
    file_path = create_path()
    dir_names = file_path.split('/')
    if '.' in file_path and len(dir_names) == 1:
        write_to_file(file_path)
    elif '.' not in file_path:
        create_directory(dir_names)
    else:
        create_directory(dir_names[:-1])
        write_to_file(file_path)


if __name__ == "__main__":
    create_file()
