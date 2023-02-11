#!/usr/bin/env python3
from gendiff import generate_diff, parse_cli_data


def main():
    file1, file2 = parse_cli_data()
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
