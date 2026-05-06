import datetime
import sys
import os

incoming_command = sys.argv[1:]


def create_file(start_position, pwd):
    if incoming_command[0] == "-f":
        filename = incoming_command[start_position + 1]
        os.chdir(pwd)
        new_file = open(filename, "a")
        input_list = []
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                new_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                new_file.close()
                for number, line in enumerate(input_list, start=1):
                    new_file.write(f"{number} {line}\n")
                break
            input_list.append(user_input)


if __name__ == "__main__":
    if "-d"in incoming_command and "-f" in incoming_command:
        d_index = incoming_command.index("-d")
        f_index = incoming_command.index("-f")

        path_parts = incoming_command[d_index: f_index]
        directory_path = os.path.join(*path_parts)
        os.makedirs(directory_path)
        create_file(f_index, directory_path)

        print(incoming_command)
        print(d_index)
        print(f_index)
        print(directory_path)

