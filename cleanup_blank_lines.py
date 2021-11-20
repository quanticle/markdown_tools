import pathlib
import re
import sys


def cleanup_blank_lines_in_lists(filename):
    output_lines = []
    with open(filename, 'r', encoding="utf-8") as read_file:
        input_lines = [line.rstrip() for line in read_file.readlines()]
        i = 1
        output_lines.append(input_lines[0])
        while i < len(input_lines):
            prev_line = input_lines[i - 1]
            cur_line = input_lines[i]
            if (re.match(r'^ *-', prev_line) or re.match(r'^ *`', prev_line)) and len(cur_line) == 0:
                pass
            elif re.match(r'^#', cur_line):
                output_lines.append("")
                output_lines.append(cur_line)
            else:
                output_lines.append(cur_line)
            i += 1

    with open(filename, 'w', encoding="utf-8") as write_file:
        write_file.write("\n".join(output_lines))


def cleanup_markdown_directory(directory_name):
    markdown_paths = pathlib.Path(directory_name).rglob(r'*.md')
    for path in markdown_paths:
        cleanup_blank_lines_in_lists(path)


if __name__ == '__main__':
    cleanup_markdown_directory(sys.argv[1])