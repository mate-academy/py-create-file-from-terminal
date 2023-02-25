from argparse import ArgumentParser
from os import makedirs, path
from datetime import datetime

parser = ArgumentParser()
parser.add_argument("-d", "--directory", nargs="*")
parser.add_argument("-f", "--file")
args = parser.parse_args()


if args.directory:
    args.directory = "/".join(args.directory)
    makedirs(args.directory, exist_ok=True)
if args.file:
    dir_path = (args.file if not args.directory
                else path.join(args.directory, args.file))
    with open(dir_path, "a") as file:
        now = datetime.now()
        file.write(f"{now.strftime('%y-%m-%d %H:%M:%S')}\n")
        num = 1
        text = f"{num} {input('Enter content line: ')}\n"
        while text != f"{num} stop\n":
            file.write(text)
            num += 1
            text = f"{num} {input('Enter content line: ')}\n"
        file.write("\n")
