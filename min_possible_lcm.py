from math import gcd

n = int(input())
a = list(map(int, input().split()))
minimum = 100000000
res_1 = 0
res_2 = 0
for i in range(n):

    for j in range(i+1, n):
        lcm = (a[i]*a[j])/gcd(a[i],a[j])
        if lcm < minimum:
            minimum = lcm
            res_1 = i
            res_2 = j
print(res_1+1,res_2+1)
