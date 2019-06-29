from sys import stdin, stdout

def main_job():
    l=[]
    n,m= stdin.readline().split()
    n=int(n)
    m=int(m)
    for i in range(n):
        t= int(input().split())
        l.append(t)
    x=int(input())
    if x in l:
        print("yes")


if __name__ == "__main__":
    main_job()
