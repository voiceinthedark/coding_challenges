# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    l = sorted(l, key=lambda x: x[1])
    mins = sorted(list(set([a[1] for a in l])))
    
    l = sorted([a[0] for a in l if a[1] == mins[1]])    
    for i in l:
        print(i)

    
