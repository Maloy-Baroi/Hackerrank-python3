from collections import defaultdict

n = int(input())
d = defaultdict(int)
for i in range(n):
    keys = input()
    d[keys] += 1
print(len(d))
print(*d.values())
