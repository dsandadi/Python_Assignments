#!/usr/bin/env python
import sys
import re
import collections
import operator

def extractFile():
    f = open("G:\\NIU_Masters\\Semester 3\\Artificial Intelligence\\Assignments\\74.txt"
             , encoding='iso-8859-1')
    return f.read()


def cleanFile():
    contents = extractFile()
    contents = re.sub(r'--', "  ", contents)
    contents = re.sub(r'[^\w-]', " ", contents).lower()
    print(contents)
    return contents

def createDict(file):
    dict = {}
    for i in file:
        if(not i.isalpha()):continue
        if(i in dict):
            dict[i] = dict[i]+ 1
        else:
            dict[i] = 1
    return dict

def printArguments():
    print("Command Line Arguments are :", sys.argv[1],
          "\n ", sys.argv[2])


if (__name__ == '__main__'):

    # printArguments()
    contents = cleanFile()

    dict = createDict(contents)

    dict = collections.OrderedDict(sorted(dict.items()))

    print('sorted by Key :')

    for a in dict.items():
        print(a)

    print('sorted by value :')

    sorted_dict = sorted(dict.items(),reverse=True, key=operator.itemgetter(1))
    for tuple in sorted_dict:
        print(tuple)

