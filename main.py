#!/usr/bin/env python3
import argparse


def main():
    text = "This is a test program to \
    use the command line arguments"

    parser = argparse.ArgumentParser(description=text)

    parser.add_argument(
        "-V", "--version", help="show program version", action="store_true"
    )

    parser.add_argument("-n", "--number", help="print thomas n times")

    args = parser.parse_args()

    if args.version:
        print("This is main version 0.1")
    elif args.number:
        n = int(args.number)
        for i in range(n):
            print("thomas")


if __name__ == "__main__":
    main()
