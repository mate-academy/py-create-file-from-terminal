import os
import sys
from datetime import datetime


def create_file(data):
    file_path = []
    if '-d' in data:
        for i in range(data.index('-d') + 1, len(data)):
            if data[i] == '-f':
                break
            file_path.append(data[i])
    os.makedirs(os.path.join(*file_path))

    if "-f" in data:
        file_path.append(data[data.index('-f') + 1])

        with open(os.path.join(*file_path), 'a') as new_file:
            new_file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            new_file.write('\n')
            line_number = 1
            while True:
                user_input = input("Enter content line: ")
                if user_input == 'stop':
                    return
                new_file.write(f'{line_number} {user_input} \n')
                line_number += 1


create_file(sys.argv)
