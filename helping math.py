
s = input()
arr = []
neg = 0
for i in s:
    if i != '+':
        arr.append(i)
    else:
        neg+=1
        arr.append("-")

#print(neg)
arr.sort()
a = arr[neg:]
#print(arr[2])
for i in range(0, len(a)-1):
    a[i] = a[i] + "+"

print("".join(a))

