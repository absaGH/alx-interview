#!/usr/bin/python3
'''Python script to parse log and display stat'''
import sys
import re
from collections import Counter

if __name__ == "__main__":
    flsz = 0
    count = 0
    lst = []
    frq = {}

    def printstat():
        '''function to printout the stats from the log'''
        print('File size: ' + str(flsz))
        frq = Counter(lst)
        frq = sorted(frq.items())
        frq = dict(frq)
        for item in frq:
            if int(item) in [200, 301, 400, 401, 403, 404, 405, 500]:
                print(item + ': ' + str(frq[item]))

    try:
        for line in sys.stdin:

            line = line.strip()
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})( - )\[\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}.\d+\] ("\w+ \/\w+\/\d{1,3} \w+\/1.1") \d{3} \d+'
            if re.search(pattern, line):
                line = re.split(r'\s', line)
                count = count + 1
                flsz = flsz + int(line[-1])
                lst.append(line[-2])
                frq = Counter(lst)
                if (count % 10 == 0):
                    printstat()
        if count % 10 != 0:
            printstat()
    except KeyboardInterrupt:
        printstat()
        raise
