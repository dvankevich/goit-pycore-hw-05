import os, sys, argparse
from pathlib import PurePath, Path

def main():
    parser = argparse.ArgumentParser(
        description='Log file analizer.')
    # Required arguments
    parser.add_argument('file', help='The log file')

    # Optional argument with choices
    parser.add_argument('-l', '--loglevel', choices=['INFO', 'ERROR', 'DEBUG', 'WARNING'], help='The log level. If not specified, all messages are displayed')

    # Parse the command line arguments
    args = parser.parse_args()

    print(args)



if __name__ == "__main__":
    main()