# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:52:56 2017

@author: marsic
"""

######### Problem 1: Counting Vowels

s = 'azcbobobegghakl'
vowels = ['a', 'e', 'i', 'o', 'u']
numVowels = 0
for i in s:
    if i in vowels:
        numVowels +=1
print('Number of vowels:' + str(numVowels))

### OR
s = 'azcbobobegghakl'
numVowels = sum([1 if i in 'aeiou' else 0 for i in s])
print('Number of vowels:'+ str(numVowels))


######## Problem 2: Counting 'bob's
s = 'azcbobobegghakl'
nBob = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        nBob +=1
print('Number of times bob occurs is: ' + str(nBob))

### OR
s = 'azcbobobegghakl'
nBob = sum([1 if s[i:i+3] == 'bob' else 0 for i in range(len(s))])
print('Number of times bob occurs is: ' + str(nBob))


############### Practice Again - Problem 3: Alphabetical Substrings
s = 'gqmjdfnillt'
loSubStr = ''
curSubStr = s[0]
for i in range(len(s)-1):
    if curSubStr[-1] <= s[i+1]:
        curSubStr += s[i+1]
    else:
        if len(curSubStr) > len(loSubStr):
            loSubStr = curSubStr
        curSubStr = s[i+1]
if loSubStr == '': loSubStr = curSubStr
print('Longest substring in alphabetical order is: ' + loSubStr)