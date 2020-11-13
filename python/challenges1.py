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
# Count the Lone Ones
# Create a function which counts how many lone 1s appear in a given number. 
# Lone means the number doesn't appear twice or more in a row.

import re

def count_lone_ones(n):
    return len([a for a in re.split('[^1]+', str(n)) if a == '1'])


count_lone_ones(101)
count_lone_ones(1191)
count_lone_ones(462)

# %%
# Find the Difference
# You are given two strings s and t. String t is generated 
# by randomly shuffling string s and then adding one more 
# letter at a random position. Return the letter that was 
# added to t.

from itertools import zip_longest

def find_the_difference(t1, t2):
    return [b for a, b in zip_longest(sorted(t1), sorted(t2)) if a != b][0]

find_the_difference("abcd", "abcde")
find_the_difference("", "y")
find_the_difference("ae", "aea")

# %%
# Sharing is Caring
# Given a list of numbers, create a function that removes 
# 25% from every number in the list except the smallest 
# number, and adds the total amount removed to the 
# smallest number.

def show_the_love(l):
    n = sum([a/4 for a in l if a != min(l)])
    l = [a + n if a == min(l) else a - a/4 for a in l]
    return l

show_the_love([4, 1, 4])

# %%
# Vowel to Vowel Links

# Given a sentence as txt, return True if any two adjacent 
# words have this property: One word ends with a vowel, 
# while the word immediately after begins with a 
# vowel (a e i o u).

def vowel_links(txt):
    txt = txt.split()
    return any([1 if txt[i+1][0] in 'aeiou' and txt[i][-1] in 'aeiou' else 0 for i in range(len(txt)-1)])

vowel_links("a very large appliance")
vowel_links("the sudden applause")

# %%
# Check That Input Type Is the Same

# Create a function that checks if the given arguments are of the same type. 
# Return True if they are and False if they're not.

def compare_data(*args):
    return len(set([type(a) for a in args])) in [1, 0]

compare_data(1, 6, 5, 3, 7, 9)
compare_data()

#%%
# Sum of Negative Integers

# Create a function that takes a string containing integers 
# as well as other characters and return the sum of 
# the negative integers only.
import re

def negative_sum(txt):
    return sum([int(a) for a in re.split('(-\d+)', txt) if a.startswith('-')])

negative_sum("-12 13%14&-11")
negative_sum("22 13%14&-11-22 13 12")

# %%
# Array Chunking

# Given an array and chunk size "n", Create a function 
# such that it divides the array into many subarrays where 
# each subarray is of length size "n".

def chunk(l, n):
    return [l[i-n:i] for i in range(n, len(l) + n, n)]

chunk([1, 2, 3, 4], 2)
chunk([1, 2, 3, 4, 5, 6, 7], 3)
chunk([1, 2, 3, 4, 5], 10)

# %%
# Length of Number

def number_length(n):
    return sum(1 for a in str(n))

number_length(10)
# %%
# Broken Keyboard

from collections import OrderedDict

def find_broken_keys(t1, t2):
    o = OrderedDict(zip(t1, t2))
    return [a for a, b in o.items() if a != b]

find_broken_keys("starry night", "starrq light")
find_broken_keys("mozart", "aiwgvx")
find_broken_keys("happy birthday", "hawwy birthday")

# %%
# Recursion: Halve and Halve Again

def halve_count(a, b):
    if a > b:
        return halve_count(a/2, b) + 1
    return -1

halve_count(1324, 98)

# %%
# Ones and Zeroes
# Write a function that returns True if every consecutive 
# sequence of ones is followed by a consecutive sequence of 
# zeroes of the same length.
import re 

def same_length(txt):
    return all(len(a) == len(b) for a, b in 
        zip(re.findall('1+', txt), re.findall('0+', txt))) and len(txt) % 2 == 0
    

same_length("110011100010")
same_length('1001')
same_length('101')

# %%
# Luke, I Am Your ...

def relation_to_luke(name):
    d = {'Darth Vader': 'father', 'Leia': 'sister',
        'Han': 'brother in law', 'R2D2': 'droid'}
    return "Luke, I am your {}.".format(d.get(name))

relation_to_luke("Darth Vader")

# %%
