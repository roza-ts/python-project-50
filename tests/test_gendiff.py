from gendiff import generate_diff
import pytest


@pytest.fixture
def file1():
    file = "tests/fixtures/file1.json"
    return file


@pytest.fixture
def file2():
    file = "tests/fixtures/file2.json"
    return file


@pytest.fixture
def file_string():
    with open("tests/fixtures/string.txt") as file:
        return ''.join(file.readlines())[:-1]


def test_generate_diff(file1, file2, file_string):
    assert generate_diff(file1, file2) == file_string
