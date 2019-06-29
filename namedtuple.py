from collections import OrderedDict
n=int(input())
orderdict = OrderedDict()
for i in range(n):
    k,l,v = input().rpartition(' ')
    orderdict[k] = orderdict.get(k,0) + int(v)

for i in orderdict:
    print(i, orderdict[i])
