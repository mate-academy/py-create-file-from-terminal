from datetime import datetime
from os import path, makedirs
from sys import argv


def create_file(name: str) -> None:
    with open(name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            text = input("Enter new line of content: ")
            if text != "stop":
                file.write(text + "\n")
            else:
                file.write("\n")
                break


def main() -> None:
    input_args = argv[1:]
    if "-d" in input_args:
        if "-f" in input_args:
            input_args.pop(input_args.index("-f"))
            makedirs(path.join(*input_args[1:-1]), exist_ok=True)
            if path.isdir(path.join(*input_args[1:-1])) is False:
                raise ValueError("can't create directory destination")
            create_file(path.join(*input_args[1:]))
    elif "-f" in input_args:
        create_file(input_args[input_args.index("-f") + 1])
    else:
        raise ValueError("Should be one of '-f' or '-d' parameters!")


if __name__ == "__main__":
    main()
