import argparse
import re
from pathlib import Path
from sys import exit

COLOR_WARNING = "\033[31m"
COLOR_BOLD = "\033[1m"
COLOR_END = "\033[0m"


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

    def parse_args(self):
        self.parser.add_argument(
            "pattern",
            help="searches for PATTERN in each FILE"
        )
        self.parser.add_argument(
            "file",
            help='provide file for search'
        )

        self.args = vars(self.parser.parse_args())
        self.path = self.args.get('file')
        self.pattern = self.args.get('pattern')

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
        pattern = r"{}".format(self.pattern)
        result = re.search(pattern, string)

        if result:
            result = result.group()
            colored_result = COLOR_WARNING + COLOR_BOLD + result + COLOR_END
            string = string.replace(result, colored_result)
            print(string, end="")

grep = Grep()
grep.start()
