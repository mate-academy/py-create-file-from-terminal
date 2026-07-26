import sys
import os
import datetime


def create_folders(argv: list[str]) -> str:
    if "-d" not in argv:
        return ""

    start = argv.index("-d") + 1
    end = argv.index("-f") if "-f" in argv else len(argv)

    parts = argv[start:end]
    path = os.path.join(*parts)

    os.makedirs(path, exist_ok=True)
    return str(path)


def get_user_data() -> list:
    data = []
    while (user_input := input("Enter content line: ")) != "stop":
        data.append(user_input)

    return data


def write_to_file(file_out: str, data: list) -> None:
    now = datetime.datetime.now()
    with open(file_out, "a") as f_out:
        if f_out.tell() != 0:
            f_out.write("\n")
        f_out.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for index, line in enumerate(data):
            f_out.write(f"{index + 1} {line}\n")


if __name__ == "__main__":
    folders = create_folders(sys.argv)

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        file_path = os.path.join(folders, file_name)
        user_data = get_user_data()
        write_to_file(file_path, user_data)
