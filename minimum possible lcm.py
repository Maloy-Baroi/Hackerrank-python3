from math import gcd

n = int(input())
a = list(map(int, input().split()))
minimum = 100000000
res_1 = 0
res_2 = 0
x = sorted(a, reverse=True)

min_x = x[-1]
min_x2 = x[-2]
for i in range(n):
    if a[i] == min_x:
        res_1 = i
    elif a[i] == min_x2:
        res_2 = i

print(res_1+1, res_2+1)
