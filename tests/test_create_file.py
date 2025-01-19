import os
import subprocess
import shutil


def test_create_directory():
    # Test directory creation
    dir_path = "test_dir"
    subprocess.run(["python", "app/create_file.py", "-d", dir_path])
    assert os.path.isdir(dir_path)
    shutil.rmtree(dir_path)  # Clean up


def test_create_file():
    # Test file creation
    file_name = "test_file.txt"
    process = subprocess.Popen(
        ["python", "app/create_file.py", "-f", file_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # Simulate user input for content
    input_data = "Line1 content\nLine2 content\nstop\n"
    process.communicate(input=input_data)
    assert os.path.isfile(file_name)
    os.remove(file_name)  # Clean up


def test_create_dir_and_file():
    # Test directory and file creation
    dir_path = "test_dir"
    file_name = "test_file.txt"
    full_path = os.path.join(dir_path, file_name)
    process = subprocess.Popen(
        ["python", "app/create_file.py", "-d", dir_path, "-f", file_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # Simulate user input for content
    input_data = "Line1 content\nstop\n"
    process.communicate(input=input_data)
    assert os.path.isfile(full_path)
    with open(full_path, "r") as f:
        content = f.read()
    assert "Line1 content" in content
    shutil.rmtree(dir_path)
