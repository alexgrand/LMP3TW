import argparse
from pathlib import Path
from sys import exit


class Find(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.path_obj = Path()
        self.path = ''
        self.cmds = []
        self.args = {}

    def start(self):
        self.parse_args()
        self.sort_args()
        self.check_path()

    def parse_args(self):
        self.parser.add_argument(
            "find",
            help="search for files in a directory hierarchy")

        self.args = vars(self.parser.parse_args())
        return self.args

    def sort_args(self):
        for cmd in self.args:
            self.cmds.append(cmd)

            if cmd == 'find':
                self.path = self.args.get(cmd)
        return self.cmds, self.path

    def check_path(self):
        self.path_obj = Path(self.path)
        if not self.path_obj.exists():
            print(f"find: ‘{self.path}’: No such file or directory")
            exit(1)

finder = Find()
finder.start()
print(finder.args)
print(finder.cmds, finder.path)
