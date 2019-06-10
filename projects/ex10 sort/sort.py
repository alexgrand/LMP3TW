import argparse
from pathlib import Path

lines = []


def parse_args():
    """
    return args from command prompt
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        help="reverse sort"
    )
    parser.add_argument(
        '-f',
        help="ignore case",
        action="store_true"
    )
    return vars(parser.parse_args())


def sort(args):
    values = list(args.values())
    if not (values.__contains__(None) and values.__contains__(False)):
        pass
    else:
        while True:
            try:
                line = input() + '\n'
                lines.append(line)
            except:
                break

args = parse_args()
sort(args)

print("".join(sorted(lines)), end="")
