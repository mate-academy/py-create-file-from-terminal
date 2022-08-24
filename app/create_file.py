import datetime
import sys
import os


def create_path(arr):
    arr_dir = [os.path.dirname(os.path.abspath(__file__))]
    add = False
    for arg in arr:
        if arg == '-d':
            add = True
            continue
        if not add:
            continue
        if arg == '-f':
            break
        if add:
            arr_dir.append(arg)

    return os.path.join(*arr_dir)


if '-d' in sys.argv and '-f' in sys.argv:
    print("both flags are present. Create directories and file")
    path = create_path(sys.argv)
    print(path)
    os.makedirs(path, exist_ok=True)
    path = os.path.join(path, sys.argv[-1])
elif '-d' in sys.argv:
    print("Only flag '-d' is present. Create directories")
    path = create_path(sys.argv)
    os.makedirs(path)
elif 'if' in sys.argv:
    print("Only flag '-f' is present. Create file")
    path = sys.argv[2]
if '-f' in sys.argv:
    with open(path, 'at', newline='\n') as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        num = 1
        res = ""
        while True:
            res = input("Enter content line:")
            if res == "stop":
                break
            f.write(f"{num} {res}\n")
            num += 1
        f.close()
