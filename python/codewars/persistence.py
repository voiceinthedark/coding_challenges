
# Persistent Bugger.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

# Write a function, persistence, that takes in a 
# positive parameter num and returns its multiplicative 
# persistence, which is the number of times you must 
# multiply the digits in num until you reach a single digit.

from functools import reduce

def persistence(num):
    if len(str(num)) == 1:
        return 0
    return 1 + persistence(reduce(lambda x, y: int(x) * int(y), [a for a in str(num)]))

print(persistence(39))
print(persistence(999))

