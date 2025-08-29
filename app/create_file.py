import sys
import os
import datetime


del sys.argv[0]


def f_flag(directory: str = None) -> None:
    filename = sys.argv[sys.argv.index("-f") + 1]
    if directory:
        filename = os.path.join(*directory, filename)

    with open(filename, "a") as f:
        check_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(check_time + "\n")
        count = 1
        while True:
            input_value = str(input("Enter content line: "))
            if input_value == "stop":
                f.write("\n")
                break
            f.write(f"{count} {input_value}\n")
            count += 1


def d_flag() -> list:
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
    else:
        f_index = None
    directory = os.path.join(*sys.argv[1:f_index])
    os.makedirs(directory, exist_ok=True)
    return sys.argv[1:f_index]


if "-d" in sys.argv and "-f" in sys.argv:
    f_flag(d_flag())
if "-d" in sys.argv[0]:
    d_flag()
if "-f" in sys.argv[0]:
    f_flag()
