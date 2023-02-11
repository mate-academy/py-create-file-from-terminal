import os

from writer_text import writer_text
from create_argparser import create_argparser


def main() -> None:
    parser = create_argparser()
    args = parser.parse_args()

    path_dir = None
    path_file = None

    if args.createdir:
        path_dir = os.path.join(*args.createdir)
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
