
for i in range(int(input())):
    s = input()
    l = len(s)
    s = s.replace('a', '').replace('z', '').split()
    c = 0
    for j in s:
        k = len(j)
        c+=(k*(k+1)//2)
    print((l*(l+1)//2)-c)

