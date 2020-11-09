#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
'''
Anagrams
sequence of numbers that can be formed by rearranging the digits of a string
Given a string that consists of only digits modify the first half of the sring so that
it is an anagram of the second half.

determine the minimum number of opertions needed to complete the task

the following is one operation:
replace any digits in the string with any other digit(0-9)

'''

def subString(s):
    first = []
    second = []
    for i in range (0, (len(s))//2):
        a = s[i]
        first.append(a)
    for i in range (len(s)//2,len(s)):
        a = s[i]
        second.append(a)
    return first, second
    


def getAnagram(s):
    aux = subString(s)
    f = aux[0]
    s = aux[1]
    # Write your code here
    f.sort()
    s.sort()
    lista_aux = list(set(f) - set(s))
    lista = set(f) & set (s)
    return len(lista)

    
if __name__ == '__main__':
    s1 = '123456'
    s2 = '2133326615727117001540261141407327120031612260317493998987993857958996993904815918596499598790384428'

    a = subString(s1)
    print(a)
    b = getAnagram(s1)
    print(b)


    a = subString(s2)
    print(a)
    b = getAnagram(s2)
    print(b)
    #s2 = 30
    #s3 = 569

    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getAnagram(s)

    fptr.write(str(result) + '\n')
    
    fptr.close()
    '''
