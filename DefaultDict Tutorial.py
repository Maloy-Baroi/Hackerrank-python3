
from collections import defaultdict
A = defaultdict(list)
n, m = map(int,input().split())
for i in range(0,n):
    x = input()
    A[x].append(i+1)
B = []
for i in range(0,m):
    y = input()
    B.append(y)

for i in B:
    if i in A:
        print(*A[i])
    else:
        print(-1)