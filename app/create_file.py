import sys
from datetime import datetime
import os


def validation(arguments: list) -> tuple:
    if len(arguments) == 1:
        raise ValueError("-d or -f expected")

    if arguments[1] not in ["-f", "-d"]:
        raise ValueError("first parameter should be -f or -d")

    if arguments[-1] in ["-f", "-d"]:
        raise ValueError(f"Must introducing parameters for {arguments[-1]}")

    if arguments.count("-d") > 1:
        raise ValueError("So many -d arguments")

    if arguments.count("-f") > 1:
        raise ValueError("So many -f arguments")

    index_f = arguments.index("-f") if "-f" in arguments else False
    index_d = arguments.index("-d") if "-d" in arguments else False

    if index_f:
        if index_d == index_f + 1:
            raise ValueError("Expected file name name after -f")

    if index_d:
        if index_f == index_d + 1:
            raise ValueError("Expected directory name after -d")

    return (index_f, index_d)


def create_folders(
    path: str,
    arguments: list,
    index_d: int,
    index_f: int | bool,
) -> str:
    if not index_f or index_f < index_d:
        end_for = len(arguments)
    else:
        end_for = index_f
    for i in range(index_d + 1, end_for):
        path = os.path.join(path, arguments[i])
        if not os.path.exists(path):
            os.mkdir(path)

    return path


def get_date() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def input_lines() -> str:
    text = ""
    count = 1
    while True:
        new_line = input("Enter content line:")
        if new_line.lower() == "stop":
            break
        new_line = new_line.strip()
        if new_line:
            text += f"{str(count)} "
            text += f"{new_line}\n"
            count += 1
    return text


def main() -> None:
    index_f, index_d = validation(sys.argv)
    arguments = sys.argv
    path = os.getcwd()
    if index_d:
        path = create_folders(path, arguments, index_d, index_f)
    if index_f:
        text = input_lines()
        if text:
            path = os.path.join(path, arguments[index_f + 1])
            now = get_date()
            output_text = f"{now} \n"
            output_text += f"{text}\n"
            try:
                with open(path, "a") as file:
                    file.write(output_text)
            except Exception as e:
                print(e)
        else:
            error = "There is no text to "
            error += f"create or add to {arguments[index_f + 1]}"
            raise ValueError(error)
    return


if __name__ == "__main__":
    main()
