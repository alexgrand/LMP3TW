import argparse
import os.path

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

args = parser.parse_args()
fl_name = args.cat


def file_exists(fl_name):
    if os.path.exists(fl_name):
        return True
    else:
        print(f"cat: {fl_name}: No such file or directory!")
        return None


def read_file(fl_name):
    if file_exists(fl_name):
        fl = open(fl_name, 'r')
        fl_content = fl.read()
        fl.close()
        return fl_content


def read_lines(fl_name):
    if file_exists(fl_name):
        fl = open(fl_name, 'r')
        fl_content = []

        for line in fl:
            fl_content.append(line)

        fl.close()
        return fl_content


def cat_b(fl_name):
    content = read_lines(fl_name)
    nw_content = []
    line_num = 0

    for line in content:
        if not line == '\n':
            line_num += 1
            nw_content.append(f"\t{line_num}  {line}")
        else:
            nw_content.append(line)

    return nw_content


def cat_A(fl_name):
    content = read_lines(fl_name)
    nw_content = []

    for line in content:
        nw_content.append(f"{line}$")

    return nw_content


def cat_print(content):
    for line in content:
        print(line)

if args.number_nonblank:
    cat_print(cat_b(fl_name))
elif args.show_all:
    cat_print(cat_A(fl_name))
else:
    print(read_file(fl_name))
