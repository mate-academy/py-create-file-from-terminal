import os
import argparse


def create_file(file_path: str, file_name: str) -> str:
    if os.path.exists(file_path):
        full_path = os.path.join(file_path, file_name)
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                f.write("")
            return f"File created at: {full_path}"
        return f"File already exists at: {full_path}"
    return "Invalid file path provided."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", required=True)
    parser.add_argument("--file_name", required=True)
    args = parser.parse_args()

    result = create_file(args.file_path, args.file_name)
    print(result)


if __name__ == "__main__":
    main()
