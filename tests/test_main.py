import sys
import pytest
from app.create_file import parse_args
import os


def test_no_args(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog'])
    dir_path, file_name = parse_args()
    assert dir_path == ""
    assert file_name == ""


def test_only_dir(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '-d', 'folder'])
    dir_path, file_name = parse_args()
    assert dir_path == "folder"
    assert file_name == ""


def test_only_file(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '-f', 'file.txt'])
    dir_path, file_name = parse_args()
    assert dir_path == ""
    assert file_name == "file.txt"


def test_dir_and_file(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '-d', 'folder', '-f', 'file.txt'])
    dir_path, file_name = parse_args()
    assert dir_path == "folder"
    assert file_name == "file.txt"


def test_dir_multiple_parts(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '-d', 'folder1', 'folder2', '-f', 'file.txt'])
    dir_path, file_name = parse_args()

    expected_path = os.path.join("folder1", "folder2")
    assert dir_path == expected_path
    assert file_name == "file.txt"
