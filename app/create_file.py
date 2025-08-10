import sys
import os
import datetime


def redactor(file_name: str | bytes) -> None:
    with open(file_name, "a") as text_file:
        content = ""
        text_file.write(
            datetime.datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S\n")
        )
        count = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            text_file.write(f"{count} {content}\n")
            count += 1


def make_directory(path: str | bytes) -> None:
    os.makedirs(path)


term_argv = sys.argv
if "-d" in term_argv and "-f" in term_argv:
    directories = term_argv[2: term_argv.index("-f")]
    path = os.path.join(*directories)
    make_directory(path)
    file_name = term_argv[-1]
    redactor(os.path.join(path, file_name))

elif "-d" in term_argv:
    make_directory("/".join(term_argv[2:]))

elif "-f" in term_argv:
    redactor(term_argv[-1])
