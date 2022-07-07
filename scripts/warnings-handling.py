import os
import re
import sys


warning_matcher = re.compile(r'.*warning[: ].*', re.I | re.S)
warnings = 0

def warnings_count():
    global warnings
    with open(os.path.join(os.getcwd(), 'build-log.txt'), 'r') as build_log:
        build_log_lines = build_log.readlines()

    for warning in build_log_lines:
        if warning_matcher.match(warning) is not None:
            print(warning_matcher.match(warning).group(0))
            warnings += 1
    return warnings

def warnings_exit_code():
    if warnings != 0:
        print("Build has warnings.")
        sys.exit(1)
    else:
        print("Build does not have warnings.")
        sys.exit(0)


if __name__ == '__main__':
    warnings_count()
    warnings_exit_code()
