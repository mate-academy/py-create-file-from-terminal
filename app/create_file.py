import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="*",
        default=[]
    )
    parser.add_argument(
        "-f",
        default="file.txt"
    )
    parsed_args = parser.parse_args()

    target_dir = ""
    if parsed_args.d:
        target_dir = "/".join(
            parsed_args.d
        )
        os.makedirs(
            target_dir,
            exist_ok=True
        )

    file_name = parsed_args.f
    if target_dir:
        target_file = (
            f"{target_dir}/"
            f"{file_name}"
        )
    else:
        target_file = file_name

    lines = []
    while True:
        try:
            content_line = input(
                "Enter content line: "
            )
            if (
                content_line
                == "stop"
            ):
                break
            lines.append(
                content_line
                + "\n"
            )
        except EOFError:
            break

    with open(
        target_file,
        "w",
        encoding="utf-8"
    ) as file_handle:
        file_handle.writelines(
            lines
        )


if __name__ == "__main__":
    main()
