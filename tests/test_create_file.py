import os
import subprocess
import shutil
import time


def test_create_dir_and_file():
    # Test directory and file creation
    dir_path = "test_dir"
    file_name = "test_file.txt"
    full_path = os.path.join(dir_path, file_name)

    # Ensure the directory doesn't exist before running the test
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    # Start subprocess
    process = subprocess.Popen(
        ["python", "app/create_file.py", "-d", dir_path, "-f", file_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Simulate user input for content
    input_data = "Line1 content\nstop\n"
    stdout, stderr = process.communicate(input=input_data)

    # Wait for the process to complete (ensure it's finished before checking the file)
    process.wait()

    # Check for errors in stderr
    if stderr:
        print(f"Error from subprocess: {stderr}")

    # Check if the directory and file are created
    assert os.path.isdir(dir_path), f"Directory {dir_path} was not created."

    # Delay to allow time for the file creation process (sometimes subprocess can take a moment)
    time.sleep(1)

    print(f"Checking if file exists at: {full_path}")
    assert os.path.isfile(full_path), f"File {full_path} was not created."

    # Optionally, check if the content is correct
    with open(full_path, "r") as file:
        content = file.read()
        assert "Line1 content" in content, "Content not written as expected."

    # Clean up the test environment
    shutil.rmtree(dir_path)
