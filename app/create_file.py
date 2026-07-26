import argparse
import os
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-f")
parser.add_argument("-d", nargs=2)
args = parser.parse_args()
new_dir = f"{args.d[0]}/{args.d[1]}"


def create_file():
     with open(args.f, "a") as f:
          time_now = datetime.now()
          current_date = time_now.strftime("%Y-%m-%d %H:%M:%S")
          f.write(current_date + "\n")
          numb_line = 1

          while True:
               content = input("Enter content line: ")

               if content == "stop":
                    f.write("\n")
                    exit()

               f.write(f"{numb_line} {content}\n")
               numb_line += 1

if args.f and args.d:

     os.makedirs(new_dir)
     os.chdir(f"{os.getcwd()}/{new_dir}")
     create_file()

if args.d:
     os.makedirs(new_dir)

if args.f:
     create_file()

