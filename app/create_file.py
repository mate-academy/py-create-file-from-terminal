import os
import sys
import datetime


def input_parser(flow: list) -> None:
    path = os.getcwd()

    if "-d" in flow and "-f" in flow:
        path = os.path.join(
            path, *flow[flow.index("-d") + 1:flow.index("-f"):]
        )
        create_folder(path)
        path = os.path.join(path, flow[-1])
        create_file(file_name=path)
        return

    if "-d" in flow:
        path = os.path.join(path, *flow[flow.index("-d") + 1::])
        create_folder(path)

    if "-f" in flow:
        create_file(flow[-1])


def create_folder(path: str = os.getcwd()) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        print("Input content lines.\n"
              "Type 'stop' to finish entering content.\n"
              )
        start_log_time = datetime.datetime.now()
        f.write(f"{start_log_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        counter = 1
        while True:
            user_input = input(">>>   ")
            if user_input.lower() != "stop":
                f.write(f"{counter} {user_input}\n")
                counter += 1
            else:
                f.write("\n")
                break


if __name__ == "__main__":
    input_parser(sys.argv)
