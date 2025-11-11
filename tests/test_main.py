from app.create_file import create_file


def test_create_file_creates_new_file(tmp_path):
    file_path = tmp_path
    file_name = "test.txt"
    result = create_file(str(file_path), file_name)

    expected_path = file_path / file_name
    assert expected_path.exists()
    assert expected_path.read_text() == ""
    assert f"File created at: {expected_path}" in result


def test_create_file_when_file_exists(tmp_path):
    file_path = tmp_path
    file_name = "existing.txt"
    existing_file = file_path / file_name
    existing_file.write_text("already here")

    result = create_file(str(file_path), file_name)
    assert f"File already exists at: {existing_file}" in result


def test_create_file_invalid_path(tmp_path):
    invalid_path = tmp_path / "nonexistent" / "subdir"
    file_name = "fail.txt"

    result = create_file(str(invalid_path), file_name)
    assert result == "Invalid file path provided."
