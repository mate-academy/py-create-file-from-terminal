import datetime
import sys
import os


def terminal():
    command = sys.argv
    if '-d' in command and '-f' in command:
        dir_path = command[command.index('-d') + 1]
        create_dir(dir_path)
        file_name = dir_path + "/" + command[command.index('-f') + 1]
        create_file(file_name)
        return
    if '-d' in command:
        dir_path = command[command.index('-d') + 1]
        create_dir(dir_path)
    if '-f' in command:
        file_name = command[command.index('-f') + 1]
        create_file(file_name)


def create_dir(path: str):
    os.makedirs(path)


def create_file(file_name: str):
    with open(file_name, 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + '\n')
        while True:
            content = input("Your input: ")
            if content == 'stop':
                break
            f.write(content + '\n')


terminal()
