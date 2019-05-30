import argparse
import os.path
from sys import exit

cat_help = """
            cat - concatenate files and print on the standard output
            write [file_name] and check if it exists
           """
parser = argparse.ArgumentParser()
parser.add_argument("cat", help=cat_help)
parser.add_argument("-b", "--number-nonblank",
                    action="store_true",
                    help="number nonempty output lines, overrides -n")
parser.add_argument("-A", "--show-all",
                    help="equivalent to -vET",
                    action="store_true")
parser.add_argument("-e", help="equivalent to -vE", action="store_true")

args = parser.parse_args()

fl_name = args.cat


def invalid(fl_name):
    print(f"cat: {fl_name}: No such file or directory!")
    return


def file_exists(fl_name):
    if os.path.exists(fl_name):
        return True
    else:
        return None

if not file_exists(fl_name):
    invalid(fl_name)
    exit(1)


def read_file():
    fl = open(fl_name, 'r')
    fl_content = fl.read()
    fl.close()
    return fl_content


def read_lines():
    fl = open(fl_name, 'r')
    fl_content = []

    for line in fl:
        fl_content.append(line)

    fl.close()
    return fl_content


def format_lines(content):
    nw_content = []
    for line in content:
        nw_content.append(line.replace('\n', ''))
    return nw_content


def cat_b(content):
    nw_content = []
    index = 0
    for line in content:
        if not line == '':
            index += 1
            nw_content.append(f"     {index}  {line}")
        else:
            nw_content.append(line)
    return nw_content


def cat_A(content):
    nw_content = []
    for line in content:
        if not line == '':
            nw_content.append(f"{line}$")
        else:
            nw_content.append(line.replace('', '$'))

    return nw_content


def cat_print(print_all=None, content=None):
    if print_all:
        print(read_file())
        return
    else:
        for line in content:
            print(line)


def cat_start():
    COMMANDS = {
        'number_nonblank': cat_b,
        'show_all': cat_A,
        'e': cat_A
    }
    no_commands = True
    content = format_lines(read_lines())
    used_cmds = []

    for cmd in COMMANDS:
        cmd_is_active = getattr(args, cmd)
        cmd_fn = COMMANDS.get(cmd)

        if cmd_is_active and not used_cmds.__contains__(cmd_fn):
            no_commands = False
            content = cmd_fn(content)
            used_cmds.append(cmd_fn)

    cat_print(no_commands, content)


cat_start()
