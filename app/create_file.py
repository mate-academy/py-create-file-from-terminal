from sys import argv
import os
import datetime


if ("-d" in argv) and ("-f" in argv):
    if argv.index("-d") < argv.index("-f"):
        dir_path = os.path(os.getcwd(),*argv[argv.index("-d")+1:argv.index("-f")-1])
    else:
        dir_path = os.path(os.getcwd(),*argv[argv.index("-d")+1:])
    file_name = argv[argv.index("-f")+1]
    os.makedirs(dir_path)
    os.chdir(dir_path)
    with open(file_name,"a") as file1:
        file1.write("\n")
        line = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        file1.write(line)
        row_number = 1
        line = input("Enter content line: ",)
        while line != "stop":

            file1.write(str(row_number)+line)
            line = input("Enter content line: ",)
            row_number += 1
elif "-d" in argv:
    dir_path = os.path(os.getcwd(),*argv[argv.index("-d")+1:])
    os.makedirs(dir_path)
elif "-f" in argv:
    file_name = argv[argv.index("-f")+1]
    with open(file_name,"a") as file1:
        file1.write("\n")
        line = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        file1.write(line)
        row_number = 1
        line = input("Enter content line: ",)
        while line != "stop":

            file1.write(str(row_number)+" "+line+"/n")
            line = input("Enter content line: ",)
            row_number += 1
