#! /usr/bin/python3

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
        print("{}{}".format(new_indent, match.group(2)))
    else:
        print(line.strip())

if __name__ == "__main__":
    for line in sys.stdin:
        four_to_two(line)
            
