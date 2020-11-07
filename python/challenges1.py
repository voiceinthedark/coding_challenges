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
