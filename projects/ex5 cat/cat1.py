import argparse
import os.path
import sys
from sys import exit


def invalid(fl_name):
    print(f"cat: {fl_name}: No such file or directory!")
    return


class File(object):
    def __init__(self):
        self.file = ''
        self.content = ''

    def exists(self, fl_name):
        if os.path.exists(fl_name):
            return True
        else:
            return

    def read(self, fl_name):
        if self.exists(fl_name):
            self.file = open(fl_name, 'r')
            self.content = ''
            self.content = self.file.read()
            self.file.close()
            return self.content
        else:
            invalid(fl_name)
            return

    def read_lines(self, fl_name):
        if self.exists(fl_name):
            self.file = open(fl_name, 'r')
            self.content = []

            for line in self.file:
                self.content.append(line)
            self.file.close()
            self.format_lines()
            return self.content
        else:
            invalid(fl_name)
            return

    def format_lines(self):
        nw_content = []
        for line in self.content:
            nw_content.append(line.replace('\n', ''))

        self.content = nw_content
        return self.content


class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = ''
        self.cmds = []
        self.files = []
        self.fl = File()
        self.content = []

    def parse_args(self):
        self.parser.add_argument("cat",
                                 nargs='*',
                                 help="[OPTION]... [FILE]...")
        self.parser.add_argument("-b", "--number-nonblank",
                                 action="store_true",
                                 help="number nonempty output lines")

        self.args = vars(self.parser.parse_args())
        return self.args

    def sort_args(self):
        """
        sort args into commands and files.
        return cmds and files
        """
        for arg in self.args:
            self.cmds.append(arg)

        self.files = (self.args.get('cat'))
        return self.cmds, self.files

    def check_files(self):
        for fl_name in self.files:
            if not self.fl.exists(fl_name):
                print(f"cat: {fl_name}: No such file or directory!")
                self.files.pop(self.files.index(fl_name))

    def prnt(self):
        for line in self.content:
            for ln in line:
                print(ln)

    def start(self):
        self.parse_args()
        self.sort_args()
        self.check_files()

        for cmd in self.cmds:
            if self.args[cmd]:
                fn = getattr(self, cmd)
                fn()

        self.prnt()

    def cat(self):
        if len(self.files) == 0:
            print('cat: Error: You didn\'t write any correct input!')
            exit(0)
        elif len(self.files) == 1:
            self.content.append(self.fl.read_lines(self.files[0]))
        else:
            for fl_name in self.files:
                self.content.append(self.fl.read_lines(fl_name))

    def number_nonblank(self):
        nw_content = []
        for line in self.content:
            index = 0
            nw_line = []
            for ln in line:
                if not ln == '':
                    index += 1
                    nw_line.append(f"     {index}  {ln}")
                else:
                    nw_line.append(ln)
            nw_content.append(nw_line)

        self.content = nw_content
        return self.content


parser = Parser()
parser.start()

# print('\n')
# print(">>> parser.args=", parser.args)
# print(">>> parser.cmds=", parser.cmds)
# print(">>> parser.files=", parser.files)
# print(">>> parser.content=", parser.content)
# print(">>> len(parser.content)=", len(parser.content))
