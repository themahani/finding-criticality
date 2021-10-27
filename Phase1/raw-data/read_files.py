#!/usr/bin/env python
""" Make a list of numpy data files and return them """

from glob import glob

def read_files() -> list:
    """ return the .npy files in this root directory """
    return glob("unbasket/**/*.npy")

def main():
    """ main body """
    print(len(read_files()))


if __name__ == "__main__":
    main()
