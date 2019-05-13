#!/usr/bin/env python

# in terms of complexity this python code is much simplier and easier to write out than the bash script we used previously 
# however the efficiency has been reduced due to using multple lists to store everything and the output time has increased due
# calling lower level functions

import os
import sys
import collections
import string

def main():

    # used /data/courses/ece_3822/2019_spring/eeg_reports/ as directory for testing
    x = sys.argv[1]

    # variables to hold information
    files = []
    words = []

    # used os.walk in order to fetch directories for each txt file
    for dirpath, dirnames, filenames in os.walk(x):
        for filename in [f for f in filenames if f.endswith(".txt")]:
            files.append(os.path.join(dirpath, filename))

    # open each file and then use lower and strip punctuation to get all words then store to list
    for line in files:
        fopen = open(line)
        for line in fopen:
            line = line.lower()
            line = line.translate(None, string.punctuation)
            for w in line.split():
                words.append(w)

    # count the freuqency of each word
    result = collections.Counter(words)

    # sort by most common used
    result.most_common()

    # output count
    for value, count in result.most_common():
        print(value,count)

if __name__ == "__main__": 
    main()