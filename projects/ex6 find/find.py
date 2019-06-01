import sys
import os
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("find",
                        help="search for files in a directory hierarchy")

    return vars(parser.parse_args())

u_path = parse_args().get('find')

print(os.path.exists(u_path))

