import os
import sys
import datetime


def main():
    filename = ''
    path = ''
    param = sys.argv[1:]
    if '-f' in param:
        filename = param[-1]
        param = param[:-2]
    if '-d' in param:
        path = "/".join(param[1:])
        os.makedirs(path)

    if filename:
        name = filename
        if path:
            name = f'{path}/{filename}'
        with open(name, 'a') as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.writelines(now + '\n')
            inp = ''
            while inp != 'stop':
                inp = input('input content line: ')
                if inp == 'stop':
                    break
                f.writelines(inp + '\n')


if __name__ == "__main__":
    main()
