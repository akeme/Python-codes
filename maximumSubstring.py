#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''

Maximun Substring
a sunstring is a contiguous sequence of characters within a string.
Given a string determine the aphabetically maximum substring;

example:
s = 'baca'

'''

def substrings(s):
    aux = []
    for i in range (0, len(s)+1):
        for j in range (1, len(s)+1):
            a = s[i:j]
            aux.append(a)
    
    return aux

def maxSubstring(s):
    # Write your code here
    sub = substrings(s)
    mylist = list(dict.fromkeys(sub))
    mylist.sort()
    return mylist[len(mylist)-1]

if __name__ == '__main__':

    s = 'ba'
    sub = substrings(s)
    print(sub)
    mylist = list(dict.fromkeys(sub))
    print(mylist)
    asw = maxSubstring(s)
    print('answer', asw)

'''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = maxSubstring(s)

    fptr.write(result + '\n')

    fptr.close()
'''
