import gendiff
import pytest


@pytest.fixture
def file1():
    return "tests/fixtures/file1.yaml"


@pytest.fixture
def file2():
    return "tests/fixtures/file2.yml"


@pytest.fixture
def file1_json():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file2_json():
    return "tests/fixtures/file2.json"


@pytest.fixture
def file_string():
    with open("tests/fixtures/string.txt") as file:
        return ''.join(file.readlines())[:-1]


def test_generate_diff_yaml_yml(file1, file2, file_string):
    assert gendiff.generate_diff(file1, file2) == file_string


def test_generate_diff_json(file1_json, file2_json, file_string):
    assert gendiff.generate_diff(file1_json, file2_json) == file_string
