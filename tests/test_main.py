import subprocess
from pathlib import Path

script_path = Path(__file__).parent.parent / "app" / "create_file.py"

def test_create_file_only(tmp_path):
    file_path = tmp_path / "file.txt"

    user_inputs = [
        "Line1 content",
        "Line2 content",
        "stop"
    ]

    result = subprocess.run(
        [
            "python",
            str(script_path),
            "-f",
            str(file_path.name)
        ],
        cwd=tmp_path,
        input="\n".join(user_inputs) + "\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert file_path.exists()

    content = file_path.read_text()
    assert "1 Line1 content" in content
    assert "2 Line2 content" in content


def test_create_directory_and_file(tmp_path):
    dir_path = tmp_path / "dir1" / "dir2"
    file_path = dir_path / "file.txt"

    user_inputs = [
        "Test line 1",
        "Test line 2",
        "stop"
    ]

    result = subprocess.run(
        [
            "python",
            str(script_path),
            "-d",
            "dir1",
            "dir2",
            "-f",
            "file.txt"
        ],
        cwd=tmp_path,
        input="\n".join(user_inputs) + "\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert file_path.exists()
    content = file_path.read_text()
    assert "1 Test line 1" in content
    assert "2 Test line 2" in content
