# %%
# Return Duplicate Numbers
# Given a list nums where each integer is between 1 and 100, 
# return a sorted list containing only duplicate numbers from 
# the given nums list.

def duplicate_nums(l):
    return sorted(list(set([x for x in l if l.count(x) > 1]))) or None

duplicate_nums([1, 2, 3, 4, 3, 5, 6])
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54])
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# %%
# Digit Distance
# The digit distance between two numbers is the total value 
# of the difference between each pair of digits.
# digit_distance(234, 489) ➞ 12
# Since |2 - 4| + |3 - 8| + |4 - 9| = 2 + 5 + 5

def digit_distance(n1, n2):
    nm1 = [int(x) for x in str(n1)]
    nm2 = [int(x) for x in str(n2)]
    return sum([j - i for i, j in zip(nm1,nm2)])

digit_distance(121, 599)

# %%
# Mini Sudoku

# A Sudoku is a 9x9 grid that is completed when every 
# 3x3 square, row and column consist of the numbers 1-9.
# For this task, you will be given a completed 3x3 square, 
# in the form of a two-dimensional list. Create a function 
# that checks to make sure this 3x3 square contains each 
# number from 1-9 exactly once. Make sure there are no 
# duplicates, and no numbers outside this range.

from itertools import chain

def is_mini_sudoku(l):
    return set(range(1, 10)) == set(chain(*l)) and 0 not in set(chain(*l))

is_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]])
is_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]])

# %%
# Sum of Every Nth Number
# Given a list of numbers and a positive value for n, 
# return the sum of every nth number in the list.

def sum_every_nth(l, n):
    return sum([l[i] for i in range(n-1, len(l), n)])

sum_every_nth([2, 5, 3, 9, 5, 7, 10, 7, 3, 3, 3], 9)
# sum_every_nth([4, 8, 6, 6, 7, 9, 3], 1)
sum_every_nth([4, 5, 8, 7, 8, 1, 7, 9, 7, 4, 6, 2, 8, 8, 9, 9, 1, 7, 4], 6)
sum_every_nth([10, 9, 2, 5, 9, 6, 4, 6, 7, 10, 9, 9, 9, 9, 2, 1, 2], 7)

# %%
# Encoded String Parse

# Create a function which takes in an encoded string 
# and returns a dictionary according to the following example:

# parse_code("John000Doe000123") ➞ {
#     "first_name": "John",
#     "last_name": "Doe",
#     "id": "123"
# }

def parse_code(txt):
    s = list(filter(lambda x: x != '' , txt.split('0')))
    return {'first_name': s[0],    
        'last_name': s[1],
        'id': s[2]}
    # return s

parse_code('Michael0Smith004331')

# %%
# Find the Longest Word

# Write a function that will return the longest word in 
# a sentence. In cases where more than one word is found, 
# return the first one.

import re

def find_longest(sentence):
    wlst = re.split('\W+', sentence)
    wlen = [len(a) for a in wlst]
    return max(zip(wlen, wlst), key=lambda x: x[0])[1].lower()


find_longest("A thing of beauty is a joy forever.")
find_longest("Forgetfulness is by all means powerless!")
find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.")

# %%
# Pluralize!

# Given a list of words in the singular form, return a set 
# of those words in the plural form if they appear more 
# than once in the list.

def pluralize(l):
    return set([a + 's' if l.count(a) > 1 else a for a in l])

pluralize(["cow", "pig", "cow", "cow"])

# %%
# Smallest Missing Positive Integer
# Given a list of integers, return the smallest positive integer not present in the list.


def min_miss_pos(l):
    fl = sorted([a for a in l if a >= 0])
    ll = list(set(range(1, max(fl) + 1)) - set(fl))
    if len(fl) > 1:
        if len(ll) > 0:
            return min(ll)
        else:
            return max(fl) + 1
    return 1 

min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2])
min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9])
min_miss_pos([0, -4, -4, -1, -9, -4, -5, -2, -10, -7, -6, -3, -10, -9])
min_miss_pos([7, 6, 5, 4, 3, 2, 1])

# %%
