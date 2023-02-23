#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.modules.parsing_cli_data import parse_cli_data


def main():
    file_path1, file_path2, formater = parse_cli_data()
    print(generate_diff(file_path1, file_path2, formater))


if __name__ == '__main__':
    main()
