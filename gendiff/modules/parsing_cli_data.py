import argparse


def parse_cli_data():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help="set format of output")
    args = parser.parse_args()
    formater = args.format
    if formater == 'plain':
        return args.first_file, args.second_file, 'plain'

    return args.first_file, args.second_file, formater
