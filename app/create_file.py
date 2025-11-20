import sys
import os
import datetime


def time_without_microsecond() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_args():
    """Парсимо -d і -f незалежно від порядку."""
    args = sys.argv[1:]
    dir_path_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        # беремо все, поки не зустрінемо -f або кінець
        while d_index < len(args) and args[d_index] != "-f":
            dir_path_parts.append(args[d_index])
            d_index += 1

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    return dir_path_parts, file_name


def create_dirs(dir_parts: list[str]) -> str:
    """Створює директорію з частин шляху, кросплатформно."""
    if not dir_parts:
        return ""

    path = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(dir_path: str, filename: str) -> None:
    """Створює та заповнює файл."""
    file_path = os.path.join(dir_path, filename) if dir_path else filename

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as output_file:
        line_counter = 1

        output_file.write(
            f"{time_without_microsecond()}\n"
            if os.stat(file_path).st_size == 0
            else f"\n{time_without_microsecond()}\n"
        )

        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            output_file.write(f"{line_counter} {text}\n")
            line_counter += 1


def act_command():
    dir_parts, filename = parse_args()

    dir_path = create_dirs(dir_parts) if dir_parts else ""

    if filename:
        create_file(dir_path, filename)
    elif dir_parts:
        print(f"Directory created: {dir_path}")
    else:
        print("No valid command provided.")


if __name__ == "__main__":
    act_command()
