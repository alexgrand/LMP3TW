import argparse
import re
from pathlib import Path
from sys import exit


class Grep(object):
    def __init__(self):
        self.pattern = ''
        self.strings = []
        self.results = []
        self.parser = argparse.ArgumentParser()
        self.args = []
        self.path = ''

    def start(self):
        self.parse_args()
        self.check_path()
        self.get_strings()
        self.parse_strings()
        self.prnt()

    def parse_args(self):
        self.parser.add_argument(
            "regex",
            help="grep  searches for PATTERN in each FILE"
        )
        self.parser.add_argument(
            "file",
            help='provide file for search'
        )

        self.args = vars(self.parser.parse_args())

    def check_path(self):
        fl_path = self.args.get('file')

        if not Path(fl_path).exists():
            print(f"grep: {fl_path}: No such file or directory!")
            exit(0)
        elif Path(fl_path).is_dir():
            print(f"grep: {fl_path}: Is a directory!")
            exit(0)

        self.path = fl_path
        return fl_path

    def get_strings(self):
        fl = open(self.path, 'r')
        self.strings = fl.readlines()
        fl.close()

        return self.strings

    def parse_strings(self):
        for string in self.strings:
            self.parse_str(string)

    def parse_str(self, string):
        print(string, end="")

    def prnt(self):
        for result in self.results:
            print(result, end="")

grep = Grep()
grep.start()
