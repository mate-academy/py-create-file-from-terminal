import os
import sys
from datetime import datetime


TODAY = datetime.now()
DAT_LIST = str(TODAY).split(".")
DAT = DAT_LIST[0]
TERMINAL_STR = " ".join(sys.argv)


def creater():
    with open("file.txt", "a") as file:
        file.write(DAT + "\n")
        print(os.getcwd())
        for line in sys.stdin:
            print(f'Enter content line: {line}')
            d = line.replace('stop', '')
            file.write(d)
            if 'stop' == line.rstrip():
                break


if "-d" in sys.argv and "-f" not in sys.argv:
    terminal_d = TERMINAL_STR.partition('-d ')[2]
    terminal_d_ = str(terminal_d.replace(' ', '/'))
    os.makedirs(terminal_d_)

if "-f" in sys.argv and "-d" not in sys.argv:
    creater()

if "-d" in sys.argv and "-f" in sys.argv:
    terminal_df = TERMINAL_STR.partition('-d ')[2]
    terminal_df = terminal_df.partition(' -f')[0]
    terminal_df_ = terminal_df.replace(' ', '/')
    os.makedirs(terminal_df_)
    os.chdir(terminal_df_)
    creater()
