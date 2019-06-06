import re
import sys
import argparse
from pathlib import Path


class Cut(object):
    def __init__(self):
        self.path = ''
        self.parser = argparse.ArgumentParser()
        self.args = {}
        self.strings = []
        self.activated_cmds = []
        self.available_cmds = ['']

    def invalid_option(self, option=None):
        print(f"sed: invalid option: {option}")
        print("""
        SED can be invoked in the following two forms:
        sed.py [-n] [-e] 'command(s)' files
        sed.py [-n] -f scriptfile files
        """)
        sys.exit(0)

    def start(self):
        self.parse_args()
        self.check_sed_option()
        self.get_strings()

    def parse_args(self):
        self.parser.add_argument(
            "-f", "--file",
            help="""
            add the contents of script-file to the commands to be executed
            """,
            action="store_true"
        )
        self.parser.add_argument(
            "sed",
            help="""
            stream editor for filtering and transforming text.
            """
        )
        self.parser.add_argument(
            "-e", "--expression",
            help="""
            add the script to the commands to be executed
            """,
            action="store_true"
        )
        self.parser.add_argument(
            "path_to_file",
            help="path to file"
        )

        self.args = vars(self.parser.parse_args())

    def check_sed_option(self):
        sed = self.args.get('sed')
        sed_file = self.args.get('file')
        if not (self.available_cmds.__contains__(sed) or sed_file):
            self.invalid_option(sed)

    def check_path(self, path):
        if not Path(path).exists():
            print(f"sed: can't read {path}: No such file or directory")
            sys.exit(0)

    def get_strings(self):
        self.path = self.args.get('path_to_file')
        self.check_path(self.path)
        print(self.args)

cut = Cut()
cut.start()
