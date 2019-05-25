from sys import argv


class CommandArgs(object):
    def __init__(self):
        self.len = len(argv)
        self.ls = {
            '-h':
            """
            -h --help   Help command for ARGV. Type -h or --help and then
                        command 'name' to get help.
            """,
            'sum':
            """
            sum         'sum' is used to sum 2 arguments and more. ex: sum 1 2
            """
        }
        self.commands = {
            '-h': self.help,
            '--help': self.help,
            'sum': self.sum
        }

    def show(self):
        for text in self.ls.values():
            print(text)

    def invalid(self):
        print(f"\n\tInvalid command. Try -h or --help.\n")

    def get(self, command):
        text = self.ls.get(command)
        if text:
            return text
        return self.invalid()

    def prnt(self, command):
        print(self.get(command))

    def help(self):
        if self.len == 2:
            self.show()
        elif self.len == 3:
            command = self.ls.get(argv[2])
            if command:
                print(command)
            else:
                self.invalid()
        else:
            self.invalid()

    def sum(self):
        if self.len < 4:
            self.prnt('sum')
        else:
            argv.pop(0)
            argv.pop(0)
            total = 0
            for arg in argv:
                try:
                    arg = int(arg)
                    total += arg
                except ValueError:
                    print("\n\tError! Arguments for 'sum' must be integers\n")
                    return
            print('\n\t', total, '\n')

    def check(self):
        if self.len == 1:
            self.invalid()
        if self.len > 1:
            cm = self.commands.get(argv[1])
            if cm:
                cm()
            else:
                self.invalid()


commands = CommandArgs()
commands.check()
