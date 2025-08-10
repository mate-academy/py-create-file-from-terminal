import sys
from datetime import datetime
from pathlib import Path


def write_data(file_name: Path) -> None:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(formatted_time + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(line + "\n")


def init_data(data: list) -> None:
    cmd1 = data.pop(0)
    cmd2 = None

    if "-f" in data:
        cmd2 = data.pop(data.index("-f"))

    dst_dir = Path(*data).parent
    dst_file = Path(*data)

    match cmd1, cmd2:
        case ("-d", None):
            dst_dir.mkdir(parents=True, exist_ok=True)
        case ("-f", None):
            write_data(dst_file)
        case ("-d", "-f"):
            dst_dir.mkdir(parents=True, exist_ok=True)
            write_data(dst_file)


if __name__ == "__main__":
    init_data(sys.argv[1:])
