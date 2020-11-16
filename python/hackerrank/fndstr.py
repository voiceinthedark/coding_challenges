# Find a string
# https://www.hackerrank.com/challenges/find-a-string/problem

# In this challenge, the user enters a string and a substring.
#  You have to print the number of times that the substring 
# occurs in the given string. String traversal will take 
# place from left to right, not from right to left.

def count_substring(string, sub_string):    
    indexsub = string.find(sub_string)
    if indexsub < 0:        
        return 0
    return count_substring(string[indexsub+1:], sub_string) + 1


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
