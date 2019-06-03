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
        self.pattern_obj = re.compile(self.pattern)
        self.strings = []
        self.results = []
        self.parser = argparse.ArgumentParser()
        self.args = []
        self.path = ''
        self.cmds = []

    def start(self):
        self.parse_args()
        self.check_path()
        self.get_strings()
        self.has_active_cmds()
        self.get_pattern_obj()
        self.parse_strings()

    def parse_args(self):
        self.parser.add_argument(
            "pattern",
            help="searches for PATTERN in FILE"
        )
        self.parser.add_argument(
            "file",
            help='provide file for search'
        )
        self.parser.add_argument(
            "-i", "--ignore-case",
            help="ignore case distinctions",
            action="store_true"
        )
        self.parser.add_argument(
            "-w", "--word-regexp",
            help="""
            Select only those lines containing matches that form whole words.
            The test is that the matching substring must either be at the
            beginning of the line, or preceded by  a  non-word  constituent
            character.   Similarly,  it must be either at the end of the line
            or followed by a non-word constituent character.  Word-constituent
            characters are letters, digits, and the underscore.
            This option has no effect if -x is also specified.
            """,
            action="store_true"
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

    def has_active_cmds(self):
        args = dict(self.args)
        args.pop('file')
        args.pop('pattern')

        values = list(args.values())
        if not values.__contains__(True):
            return
        else:
            self.cmds = [cmd for cmd in args.keys() if args[cmd]]

    def get_pattern_obj(self):
        pattern = r"{}".format(self.pattern)

        if not self.cmds:
            self.pattern_obj = re.compile(pattern)
            return

        if self.cmds.__contains__('ignore_case'):
            self.pattern_obj = re.compile(pattern, re.I)

    def parse_strings(self):
        for string in self.strings:
            self.parse_str(string)

    def parse_str(self, string):
        results = self.pattern_obj.findall(string)

        if results:
            for result in results:
                colored_result = COLOR_WARNING + COLOR_BOLD + result + COLOR_END
                string = string.replace(result, colored_result)
            print(string, end="")

grep = Grep()
grep.start()
