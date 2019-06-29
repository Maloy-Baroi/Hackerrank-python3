s=input()
n=int(input())

s=list(s)
l=len(s)
for i in range(l):
    x=ord(s[i])
    if x>=48 and x<=57:
        x=x+n
        if x>57:
            x=x-48
            s[i]=chr((x%10))
    elif x>=65 and x<=90:
            x=x+n
            if