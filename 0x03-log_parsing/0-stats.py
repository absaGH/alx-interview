#!/usr/bin/python3
'''Python script to parse log and display stat'''
import sys


def print_message(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        ln = line.split()
        ln = ln[::-1]

        if len(ln) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(ln[0])
                code = ln[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_lines == 10):
                print_message(codes, file_size)
                count_lines = 0

finally:
    print_message(codes, file_size)
