# sWAP cASE
# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    return ''.join([a.upper() if a.islower() else a.lower() for a in s])


if __name__ == '__main__':
    swap_case(input())
