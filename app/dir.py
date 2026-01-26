import os
from pathlib import Path


def create_directory(path: list[str]) -> Path:
    dir_path = os.path.join(*path)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path
