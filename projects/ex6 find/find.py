import argparse
from pathlib import Path
from sys import exit


class Find(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.path_obj = Path()
        self.path = ''
        self.paths = []
        self.cmds = []
        self.args = {}

    def invalid(self):
        print(f"find: ‘{self.path}’: No such file or directory")
        exit(1)

    def start(self):
        self.parse_args()
        self.sort_args()
        self.cmds_start()

    def parse_args(self):
        self.parser.add_argument(
            "find",
            help="search for files in a directory hierarchy")
        self.parser.add_argument(
            "-n", "-name", "--name",
            help="""
            pattern
                Base of file name (the path with the leading directories
                removed) matches shell pattern
            """,
            action="store_true"
        )

        self.args = vars(self.parser.parse_args())
        return self.args

    def sort_args(self):
        for cmd in self.args:
            self.cmds.append(cmd)

            if cmd == 'find':
                self.path = self.args.get(cmd)
        return self.cmds, self.path

    def path_exists(self):
        self.path_obj = Path(self.path)
        if not self.path_obj.exists():
            self.invalid()
        else:
            return True

    def cmds_start(self):
        args = dict(self.args)
        args.pop('find')
        cmd_is_active = list(args.values()).__contains__(True)

        if cmd_is_active:
            for cmd in args:
                if args[cmd]:
                    fn = getattr(self, cmd)
                    fn()
        else:
            self.find()

    def find(self):
        self.path_exists()
        print(self.path)
        return self.path

    def name(self):
        self.paths = list(Path('.').glob(self.path))

        if not self.paths:
            self.invalid()
        else:
            for path in self.paths:
                print(f"./{path}")


finder = Find()
finder.start()
# print(finder.args)
# print(finder.cmds, finder.path)
