import argparse
import os
# from sys import argv

from writer_text import writer_text


# line_argv = argv
# if "-d" in line_argv:
#     path_all = None
#     a = line_argv.index("-d")
#     if "-f" in line_argv:
#         b = line_argv.index("-f")
#         path_all = line_argv[a + 1: b]
#     else:
#         path_all = line_argv[a + 1]
#     path_dir = os.path.join(*path_all)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--createdir",
        help="Creates directory somethings inside current directory.",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--createfile",
        help="Creates some file and then terminal should"
             " ask you to input content lines until you input \"stop\"",
        type=str
    )

    args = parser.parse_args()

    path_dir = None
    path_file = None

    if args.createdir:
        path_dir = os.path.join(args.createdir)
        if not os.path.isdir(path_dir):
            os.makedirs(path_dir)

    if args.createfile:
        path_file = args.createfile
        if path_dir and path_file:
            path_file = os.path.join(path_dir, path_file)

        if os.path.isfile(path_file):  # If we have save file
            writer_text(path_file, "a")
        if not os.path.isfile(path_file):  # If we don't have this file
            writer_text(path_file, "w")


if __name__ == "__main__":
    main()
