import sys
import datetime
import os


def f_flag_func(file_name: str) -> None:
    current_date = datetime.datetime.now()
    counter_lines = 1
    with open(file_name, "a") as f:
        if os.path.getsize(file_name) != 0:
            f.write("\n")

        f.write(f"{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n")

        while True:
            string = input("Enter content line: ")
            if string == "stop":
                break

            f.write(str(counter_lines))
            f.write(" ")
            counter_lines += 1
            f.write(f"{string}\n")


def d_flag_func(directories: list) -> None:
    path = os.path.join(os.getcwd(), *directories)
    os.makedirs(path, exist_ok=True)


def main() -> None:
    input_start = sys.argv[1:]

    if "-f" in input_start and "-d" not in input_start:
        f_flag_func(input_start[1])

    if "-d" in input_start and "-f" not in input_start:
        d_flag_func(input_start[1:])

    if "-d" in input_start and "-f" in input_start:
        f_index = input_start.index("-f")
        d_flag_func(input_start[1:f_index])
        file_name_path = os.path.join(*input_start[1:f_index], input_start[-1])
        f_flag_func(str(file_name_path))


if __name__ == "__main__":
    main()
