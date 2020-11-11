# https://www.hackerrank.com/challenges/list-comprehensions/problem

x,y,z,n = 2,2,2,2

print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])


