string=input()
list1=list(string)
ans=0
for i in range(len(list1)):
    if list1[i]>='a' and list1[i]<="z":
        if list1[i]=='a':
            ans+=1
        elif list1[i]=='b':
            ans+=2
        elif list1[i]=='c':
            ans+=3
        elif list1[i]=='d':
            ans+=4
        elif list1[i]=='e':
            ans+=5
        elif list1[i]=='f':
            ans+=6
        elif list1[i]=='g':
            ans+=7
        elif list1[i]=='h':
            ans+=8
        elif list1[i]=='i':
            ans+=9
        elif list1[i]=='j':
            ans+=10
        elif list1[i]=='k':
            ans+=11
        elif list1[i]=='l':
            ans+=12
        elif list1[i]=='m':
            ans+=13
        elif list1[i]=='n':
            ans+=14
        elif list1[i]=='o':
            ans+=15
        elif list1[i]=='p':
            ans+=16
        elif list1[i]=='q':
            ans+=17
        elif list1[i]=='r':
            ans+=18
        elif list1[i]=='s':
            ans+=19
        elif list1[i]=='t':
            ans+=20
        elif list1[i]=='u':
            ans+=21
        elif list1[i]=='v':
            ans+=22
        elif list1[i]=='w':
            ans+=23
        elif list1[i]=='x':
            ans+=24
        elif list1[i]=='y':
            ans+=25
        elif list1[i]=='z':
            ans+=26
        else:
            break
    else:
        break
print(ans)