import argparse
import os
import re
import sys


parser = argparse.ArgumentParser(description='Check warnings during a build.')
parser.add_argument('-f','--file_path', help='Path to the log file.', default='build-log.txt')
args = parser.parse_args()

warning_matcher = re.compile(r'.*warning[: ].*', re.I | re.S)
warnings = 0

def warnings_count(file_path):
    global warnings
    for warnings, line in enumerate(open(file_path)):
        for match in re.finditer(warning_matcher, line):
            print(match.group(0))
            warnings +=1
    return warnings

def warnings_exit_code():
    if warnings != 0:
        print("Build has warnings.")
        sys.exit(1)
    else:
        print("Build does not have warnings.")
        sys.exit(0)


if __name__ == '__main__':
    warnings_count(args.file_path)
    warnings_exit_code()

