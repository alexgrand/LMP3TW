import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                    action="count", default=0)
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
