import sys
import os
from datetime import datetime


def create_file():
    # print("lklkl")
    command_list = sys.argv
    if "-f" not in command_list and "-d" in command_list:
        path_list = command_list[2:]
        joint_path = os.path.join(*path_list)
        os.makedirs(joint_path)
    if "-d" not in command_list and "-f" in command_list:
        if os.path.exists(command_list[2]):
            with open(command_list[2], "a") as new_content:
                content = ""
                new_content.write("\n")
                now = datetime.now()
                nice_time = now.strftime("%Y-%m-%d %H:%M:%S")
                new_content.write(f"{nice_time}\n")
                count = 0
                while content != "stop":
                    content = input("Enter content line: ")
                    if content == "stop":
                        continue
                    count += 1
                    new_content.write(f"{str(count)} {content}\n")
        else:
            with open(command_list[2], "w") as new_content:
                content = ""
                now = datetime.now()
                nice_time = now.strftime("%Y-%m-%d %H:%M:%S")
                new_content.write(f"{nice_time}\n")
                count = 0
                while content != "stop":
                    content = input("Enter content line: ")
                    if content == "stop":
                        continue
                    count += 1
                    new_content.write(f"{str(count)} {content}\n")
    if "-f" in command_list and "-d" in command_list:
        path_list = command_list[2:command_list.index("-f")]
        joint_path = os.path.join(*path_list)
        os.makedirs(joint_path)
        index_file = command_list.index("-f") + 1
        if os.path.exists(f"{joint_path}/{command_list[index_file]}"):
            with open(f"{joint_path}/{command_list[index_file]}", "a") \
                    as new_content:
                content = ""
                new_content.write("\n")
                now = datetime.now()
                nice_time = now.strftime("%Y-%m-%d %H:%M:%S")
                new_content.write(f"{nice_time}\n")
                count = 0
                while content != "stop":
                    content = input("Enter content line: ")
                    if content == "stop":
                        continue
                    count += 1
                    new_content.write(f"{str(count)} {content}\n")
        else:
            with open(f"{joint_path}/{command_list[index_file]}", "w") \
                    as new_content:
                content = ""
                now = datetime.now()
                nice_time = now.strftime("%Y-%m-%d %H:%M:%S")
                new_content.write(f"{nice_time}\n")
                count = 0
                while content != "stop":
                    content = input("Enter content line: ")
                    if content == "stop":
                        continue
                    count += 1
                    new_content.write(f"{str(count)} {content}\n")
