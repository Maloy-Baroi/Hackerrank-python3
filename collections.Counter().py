from collections import *

n = int(input())
x = list(map(int, input().split()))
x = Counter(x)
N = int(input())
total_money = 0
for i in range(N):
    a, b = map(int, input().split())
    # print(x[a])
    if x[a] != 0:
        total_money += b
        x[a] -= 1
print(total_money)
