import os


def create_directory(destination: str) -> None:
    try:
        os.makedirs(destination, exist_ok=True)
        print(f"Directory '{destination}' created successfully.")
    except FileExistsError:
        print(f"Directory {destination} already exists.")
