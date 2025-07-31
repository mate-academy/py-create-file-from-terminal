# test_create_file.py

import subprocess
import tempfile
import os
import shutil
from pathlib import Path
from app import create_file

def run_script(args: list[str], input_lines: list[str]) -> str:
    """Run create_file.py with given args and simulated input, 
    return stdout."""
    # Get the absolute path to the script and Python executable
    script_dir = Path(__file__).parent.parent
    script_path = script_dir / "app" / "create_file.py"
    python_exe = script_dir / ".venv" / "Scripts" / "python.exe"

    process = subprocess.Popen(
        [str(python_exe), str(script_path)] + args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=os.getcwd()  # Use current working directory
    )
    input_str = "\n".join(input_lines + ["stop\n"])
    stdout, stderr = process.communicate(input=input_str)
    return stdout + stderr

def test_create_file_only(tmp_path: Path) -> None:
    os.chdir(tmp_path)
    output = run_script(["-f", "test.txt"], ["Line A", "Line B"])
    file_path = tmp_path / "test.txt"
    assert file_path.exists()
    content = file_path.read_text()
    assert "Line A" in content
    assert "Line B" in content

def test_create_directory_only(tmp_path: Path) -> None:
    os.chdir(tmp_path)
    run_script(["-d", "dir1", "dir2"], [])
    dir_path = tmp_path / "dir1" / "dir2"
    assert dir_path.exists()
    assert dir_path.is_dir()

def test_create_dir_and_file(tmp_path: Path) -> None:
    os.chdir(tmp_path)
    output = run_script(
        ["-d", "dirX", "dirY", "-f", "file.txt"], 
        ["Line 1", "Line 2"]
    )
    file_path = tmp_path / "dirX" / "dirY" / "file.txt"
    assert file_path.exists()
    content = file_path.read_text()
    assert "Line 1" in content
    assert "Line 2" in content

def test_append_to_existing_file(tmp_path: Path) -> None:
    os.chdir(tmp_path)
    file_path = tmp_path / "log.txt"
    file_path.write_text("Initial content\n")

    run_script(["-f", "log.txt"], ["Appended line"])
    content = file_path.read_text()
    assert "Initial content" in content
    assert "Appended line" in content

def test_invalid_args(tmp_path: Path) -> None:
    os.chdir(tmp_path)
    result = run_script(["-f"], [])
    assert "Error: No file name provided" in result or "Usage:" in result
