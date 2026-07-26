import datetime
import sys
import os


def create_path(arr: list, both_flags=False):
    arr_dir = [os.path.dirname(os.path.abspath(__file__))]
    ind_d = arr.index("-d") + 1
    ind_f = arr.index("-f") if both_flags else len(arr)
    dir_list = arr[ind_d: ind_f]
    for arg in dir_list:
        arr_dir.append(arg)
    return os.path.join(*arr_dir)


def main():
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_path(sys.argv, True)
        os.makedirs(path, exist_ok=True)
        path = os.path.join(path, sys.argv[-1])
    elif "-d" in sys.argv:
        path = create_path(sys.argv)
        os.makedirs(path)
        return
    elif "-f" in sys.argv:
        path = sys.argv[-1]
    if "-f" in sys.argv:
        with open(path, "at", newline="\n") as file_to_write:
            cur_date = datetime.datetime.now()
            file_to_write.write(f"{cur_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
            num = 1
            res = ""
            while True:
                res = input("Enter content line:")
                if res == "stop":
                    break
                file_to_write.write(f"{num} {res}\n")
                num += 1
            file_to_write.close()


if __name__ == "__main__":
    main()
