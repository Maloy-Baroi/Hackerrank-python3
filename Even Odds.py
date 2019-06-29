
n,k = map(int, input().split())
px = (n+1)//2
if k <= px:
    print(2*k-1)
else:
    print(2*k-2*px)

