import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # parser.parse_args()
    # (['-h', 'FIRST_FILE', 'SECOND_FILE'])
    parser.print_help() #file=None)
    

if __name__ == '__main__':
    main()
