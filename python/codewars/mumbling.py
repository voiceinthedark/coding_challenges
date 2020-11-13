# Mumbling

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(t):
    return '-'.join(map(str.title, [a * (i+1) for i, a in enumerate(t)]))


accum("abcd")
accum("ZpglnRxqenU")

# %%
# Isograms

# An isogram is a word that has no repeating letters, 
# consecutive or non-consecutive. Implement a function that 
# determines whether a string that contains only letters is 
# an isogram. Assume the empty string is an isogram. 
# Ignore letter case.

def is_isogram(t):
    return len(set(t.lower())) == len(t.lower())

is_isogram("Dermatoglyphics")

# %%
# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

# Write a function that will return the count of distinct 
# case-insensitive alphabetic characters and numeric digits 
# that occur more than once in the input string. The input 
# string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    return sum(1 for a in set(text.lower()) if text.lower().count(a) > 1)


duplicate_count('aabbcde')
duplicate_count("indivisibility")





# %%
# IQ Test
# https://www.codewars.com/kata/552c028c030765286c00007d/python

# Bob is preparing to pass IQ test. The most frequent task 
# in this test is to find out which one of the given numbers 
# differs from the others. Bob observed that one number 
# usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that 
# among the given numbers finds one that is different in 
# evenness, and return a position of this number.

def iq_test(t):
    odd = [int(a) for a in t.split(' ') if int(a) % 2]
    even = [int(a) for a in t.split(' ') if not int(a) % 2]
    return t.split(' ').index(str(odd.pop())) + 1 if len(odd) == 1 else t.split(' ').index(str(even.pop())) + 1

iq_test("2 4 7 8 10")

# ! Keep in mind that your task is to help Bob solve a real 
# IQ test, which means indexes of the elements start from 1 
# (not 0)

# %%
