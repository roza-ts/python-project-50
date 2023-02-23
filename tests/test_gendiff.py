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
def result_stylish():
    with open("tests/fixtures/result_stylish.txt") as file:
        return ''.join(file.readlines())[:-1]


@pytest.fixture
def result_plain():
    with open("tests/fixtures/result_plain.txt") as file:
        return ''.join(file.readlines())[:-1]


def test_generate_diff_stylish(file1, file2, result_stylish):
    assert gendiff.generate_diff(file1, file2) == result_stylish


def test_generate_diff_plain(file1_json, file2_json, result_plain):
    assert gendiff.generate_diff(
        file1_json, file2_json, 'plain') == result_plain
