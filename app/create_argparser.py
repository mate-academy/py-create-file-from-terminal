from argparse import ArgumentParser


def create_argparser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument(
        "-d",
        "--createdir",
        help="Creates directory somethings inside current directory.",
        type=str,
        nargs="+"
    )
    parser.add_argument(
        "-f",
        "--createfile",
        help="Creates some file and then terminal should"
             ' ask you to input content lines until you input "stop"',
        type=str
    )

    return parser
