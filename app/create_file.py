import argparse
import os
from utils import create_file_only, create_directory_only


parser = argparse.ArgumentParser(description="script to create files")
parser.add_argument("-d", nargs="+")
parser.add_argument("-f")
args = parser.parse_args()


if args.d is not None and args.f is not None:
    path = create_directory_only(args.d)
    create_file_only(os.path.join(path, args.f))
elif args.d is not None:
    create_directory_only(args.d)
elif args.f is not None:
    create_file_only(args.f)
