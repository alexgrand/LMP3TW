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

args = parser.parse_args()
fl_name = args.cat


def file_exists(fl_name):
    if os.path.exists(fl_name):
        return True
    else:
        print(f"\n\tcat: {fl_name}: No such file or directory!\n")
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
    numberd_content = ''
    line_num = 0

    for line in content:
        if not line == '\n':
            line_num += 1
            numberd_content += f"\t{line_num}  {line}"
        else:
            numberd_content += line
    
    return numberd_content


if args.number_nonblank:
    print(cat_b(fl_name))
else:
    print(read_file(fl_name))
