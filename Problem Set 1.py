# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 23:21:22 2017

@author: marsic
"""

### Problem 1
#s = 'azcbobobegghakl'

numVow = sum([1 if s[i] in ['a', 'e', 'i', 'o', 'u'] else 0 for i in range(len(s))])
print("Number of vowels:", numVow)

### Problem 2
#s = 'azcbobobegghakl'

numBob = sum([1 if s[i:i+3] == "bob" else 0 for i in range(len(s))])
print("Number of times bob occurs is:", numBob)

### Problem 3
#s = 'hlqwcubrocb'
currSS = ''
lonSS = ''

for i in range(len(s)-1):
    if currSS == '':
        currSS += s[i]
    if currSS[-1] <= s[i+1]:
        currSS += s[i+1]
    elif currSS[-1] > s[i+1]:
        if len(currSS) > len(lonSS):
            lonSS = currSS
        currSS = ''
if lonSS == '' or len(currSS) > len(lonSS): lonSS = currSS
print('Longest substring in alphabetical order is:', lonSS)