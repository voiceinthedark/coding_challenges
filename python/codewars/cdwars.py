# %%
# Mumbling

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(t):
    return '-'.join(map(str.title ,[a * (i+1)  for i, a in enumerate(t)]))


accum("abcd")
accum("ZpglnRxqenU")

# %%
# Find the next perfect square!
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python

# You might know some pretty large perfect squares. 
# But what about the NEXT one?
# Complete the findNextSquare method that finds the next 
# integral perfect square after the one passed as a parameter. 
# Recall that an integral perfect square is an integer n 
# such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then - 1 
# should be returned. You may assume the parameter is 
# positive.

def findNextSquare(n):
    r = n ** (1/2)
    if r % 1 != 0:
        return - 1
    return (r+1)**2

findNextSquare(114)
findNextSquare(144)

# %%
# Array.diff
# https://www.codewars.com/kata/523f5d21c841566fde000009/python

# Your goal in this kata is to implement a difference 
# function, which subtracts one list from another and 
# returns the result.
# It should remove all values from list a, which are 
# present in list b.


def array_diff(a, b):
    return [x for x in a if x not in b]


array_diff([1, 2, 2, 2, 3], [2])
array_diff([1, 2, 2], [1])

# %%
# Does my number look big in this?
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/python

# Your code must return true or false depending upon whether 
# the given number is a Narcissistic number in base 10.

def narcissistic(n):
    return sum([int(i)**len(str(n)) for i in str(n)]) == n

narcissistic(371)
narcissistic(7)

# %%
# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da/python

# In this kata you are required to, given a string, replace 
# every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't 
# return it.

from string import ascii_lowercase

def alphabet_position(t):
    return ' '.join([str(ascii_lowercase.index(i)+1) for i in t.lower() if i.isalpha()])


alphabet_position("The sunset sets at twelve o' clock.")

# %%
# Which are in?
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

# Given two arrays of strings a1 and a2 return a sorted 
# array r in lexicographical order of the strings of a1 
# which are substrings of strings of a2.

def in_array(a, b):
    return sorted(list(set([i for j in b for i in a if i in j])))

in_array(["live", "arp", "strong"], [
         "lively", "alive", "harp", "sharp", "armstrong"])

# %%
# Delete occurrences of an element if it occurs more than n times
# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

# Given a list lst and a number N, create a new list that 
# contains each number of lst at most N times without 
# reordering. For example if N = 2, and the input is 
# [1, 2, 3, 1, 2, 1, 2, 3], you take[1, 2, 3, 1, 2], drop 
# the next[1, 2] since this would lead to 1 and 2 being in 
# the result 3 times, and then take 3, which leads 
# to[1, 2, 3, 1, 2, 3].

def delete_nth(l, e):
    r = []
    for i in l:
        if r.count(i) < e :
            r.append(i)
    return r


delete_nth([20, 37, 20, 21], 1)

# %%
# Equal Sides Of An Array
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

# You are going to be given an array of integers. Your job 
# is to take that array and find an index N where the sum 
# of the integers to the left of N is equal to the sum of 
# the integers to the right of N. If there is no index that 
# would make this happen, return -1.

def find_even_index(l):
    try:
        return [i for i in range(0, len(l)) if sum(l[:i]) == sum(l[i+1:])][0]
    except:
        return -1

find_even_index([1, 2, 3, 4, 3, 2, 1])
find_even_index([1, 100, 50, -51, 1, 1])
find_even_index([1, 2, 3, 4, 5, 6])

# %%
# Sort the odd
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers 
# must be on their places.
# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.

def sort_array(l):
    odd = [(i,j) for i,j in enumerate(l) if j % 2]
    odds = sorted(odd, key=lambda x: x[1])
    buff = []
    for i, j in zip(odd, odds):
        if j[0] not in buff:
            l[i[0]], l[j[0]] = l[j[0]], l[i[0]]
            buff.append(i[0])
    return l
    

# sort_array([5, 3, 1, 8, 0])
# sort_array([5, 3, 2, 8, 1, 4])
sort_array([2, 22, 5, 1, 4, 11, 37, 0])
sort_array([5, 1, 11, 11, 2, 1, 111, 0])

# %%
# Write Number in Expanded Form
# https://www.codewars.com/kata/5842df8ccbd22792a4000245/python

def expanded_form(n):
    fl = [i for i in str(n)][::-1]
    return ' + '.join([str(int(j) * int('1'+ '0'*i)) for i,j in enumerate(fl) if int(j) > 0][::-1])

expanded_form(42)
expanded_form(70304)

# %%
# Find the unique number
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

from itertools import groupby

def find_uniq(arr):
    return [k for k,v in groupby(arr) if len(list(v)) == 1][0]

find_uniq([1, 1, 1, 2, 1, 1])
