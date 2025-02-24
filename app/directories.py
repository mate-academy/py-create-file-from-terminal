import os


def create_directories(directory_path: str) -> None:
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory {directory_path} created successfully.")
    except FileExistsError:
        print(f"Directory {directory_path} already exists.")
