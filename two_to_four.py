from pathlib import Path
import math
import re
import sys

BEGINNING_WHITESPACE_RE = re.compile(r'^(\s+)(.*)')


def two_to_four(line):
    match = BEGINNING_WHITESPACE_RE.match(line)
    if match:
        beginning_space_count = len(match.group(1))
        indent_level = math.floor(beginning_space_count / 2)
        new_indent = '    ' * indent_level
        return "{}{}".format(new_indent, match.group(2))
    else:
        return line.strip()


def convert_file_indent(filename):
    output_lines = []
    with open(filename, 'r') as file_to_read:
        for line in file_to_read:
            output_lines.append(two_to_four(line))
    with open(filename, 'w') as file_to_write:
        file_to_write.write("\n".join(output_lines))


def convert_directory(directory_name):
    for path in Path(directory_name).rglob("*.md"):
        convert_file_indent(str(path))
