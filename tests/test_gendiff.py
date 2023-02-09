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


def test_generate_diff(file1, file2):
    assert generate_diff(file1, file2) == '''{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''

    
