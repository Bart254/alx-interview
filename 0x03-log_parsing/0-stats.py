#!/usr/bin/python3
""" Log parsing
"""
import re
import signal
import sys
from typing import Dict


# set patterns
ip_p: str = '((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}\
(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
date_p: str = r'\[\d{4}-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])' + ' ' +\
                '([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\.\d{6}\]'
str_p: str = r'"GET /projects/260 HTTP/1\.1"'
code_p: str = r'[1-5][0-9]{2}'
size_p: str = r'\d+$'

# compile the patterns into one
full_p = re.compile(rf'{ip_p} \- {date_p} {str_p} {code_p} {size_p}')

# read every line from stdin and print out results after 10 lines/ Ctrl + C
total_size: int = 0
line_no: int = 0
stats: Dict[str, int] = {"200": 0, "301": 0, "400": 0,
                         "401": 0, "403": 0, "404": 0,
                         "405": 0, "500": 0}


# set handler function for SIGINT
def handle_sigint(signum, frame):
    """ Handler function for ctrl + c
    """
    global stats, total_size
    print(f'File size: {total_size}')
    for key, value in stats.items():
        if value:
            print(f'{key}: {value}')


# Register the function for sigint
signal.signal(signal.SIGINT, handle_sigint)


for line in sys.stdin:
    # compare line to pattern
    a_match = re.match(full_p, line)

    # update dictionary, size, total_size if a match is found
    if a_match:
        line_args = line.split()
        status: str = line_args[-2]
        size: int = int(line_args[-1])
        total_size += size
        stats[status] += 1

    # print the results
    line_no += 1
    if line_no % 10 == 0:
        print(f'File size: {total_size}')
        for key, value in stats.items():
            if value:
                print(f'{key}: {value}')
