# pro02.py
from itertools import combinations
g,b=map(int,input().split())
m=len(str(g))
a=list(combinations(str(g),m-b))
a.sort()
print(*a[0],sep='')
