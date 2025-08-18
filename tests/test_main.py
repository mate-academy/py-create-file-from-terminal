import sys
import pathlib
import builtins



# Dodaj katalog główny projektu do sys.path
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from app.create_file import main

def run_main(monkeypatch, tmp_path, argv, inputs):
    """Helper: uruchamia main() z podmienionym argv i input()."""
    monkeypatch.setattr("sys.argv", ["create_file.py"] + argv)

    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))

    # ustaw bieżący katalog na tymczasowy
    monkeypatch.chdir(tmp_path)

    main()


def test_create_directory(monkeypatch, tmp_path, capsys):
    run_main(monkeypatch, tmp_path, ["-d", "dir1", "dir2"], [])
    path = tmp_path / "dir1" / "dir2"
    assert path.exists() and path.is_dir()

    captured = capsys.readouterr()
    assert "Directory created at:" in captured.out


def test_create_file(monkeypatch, tmp_path):
    file_name = "file.txt"
    run_main(
        monkeypatch,
        tmp_path,
        ["-f", file_name],
        ["Line1", "Line2", "stop"],
    )

    file_path = tmp_path / file_name
    assert file_path.exists()
    content = file_path.read_text(encoding="utf-8")
    assert "Line1" in content
    assert "Line2" in content
    assert content.startswith("20")  # timestamp


def test_append_to_existing_file(monkeypatch, tmp_path):
    file_name = "file.txt"
    file_path = tmp_path / file_name

    # pierwszy zapis
    run_main(
        monkeypatch,
        tmp_path,
        ["-f", file_name],
        ["First", "stop"],
    )
    first_content = file_path.read_text(encoding="utf-8")

    # drugi zapis (dopisek do pliku)
    run_main(
        monkeypatch,
        tmp_path,
        ["-f", file_name],
        ["Second", "stop"],
    )
    second_content = file_path.read_text(encoding="utf-8")

    assert "First" in second_content
    assert "Second" in second_content
    assert len(second_content) > len(first_content)


def test_create_directory_and_file(monkeypatch, tmp_path):
    run_main(
        monkeypatch,
        tmp_path,
        ["-d", "dirA", "dirB", "-f", "test.txt"],
        ["Hello", "stop"],
    )

    file_path = tmp_path / "dirA" / "dirB" / "test.txt"
    assert file_path.exists()
    content = file_path.read_text(encoding="utf-8")
    assert "Hello" in content
