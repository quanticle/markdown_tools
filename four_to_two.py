#! /usr/bin/env python3

# four_to_two is a little script that takes markdown text with 4-space indents on stdin and writes 2-space indented 
# markdown on stdout

import math
import re
import sys

BEGINNING_WHITESPACE_RE = re.compile(r'^(\s+)(.*)')

def four_to_two(line):
    match = BEGINNING_WHITESPACE_RE.match(line)
    if match:
        beginning_space_count = len(match.group(1))
        indent_level = math.floor(beginning_space_count / 4)
        new_indent = '  ' * indent_level
        return "{}{}".format(new_indent, match.group(2))
    else:
        return line.strip()


def print_usage_and_exit():
    print("Usage: four_to_two.py <input_file> <output_file>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage_and_exit()
    with open(sys.argv[1], 'r') as input_file:
        input_lines = input_file.readlines()
        with open(sys.argv[2], 'w') as output_file:
            for line in input_lines:
                output_file.write("{}\n".format(four_to_two(line)))
            output_file.flush()

