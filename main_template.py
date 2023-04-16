#!/usr/bin/env python3

import argparse


def main(args: argparse.Namespace):
    print(args.arg1)
    print(args.arg2)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Template to parse arguments")
    parser.add_argument("-a", "--arg1", help="An argument")
    parser.add_argument("-b", "--arg2", help="Another argument")

    args = parser.parse_args()

    if args.arg1 is None:
        parser.error("Argument arg1 is required!")

    return args


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
