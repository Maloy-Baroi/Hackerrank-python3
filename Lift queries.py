from sys import stdin, stdout

a = 0
b = 7
for i in range(int(stdin.readline())):
    x = int(stdin.readline())
    if abs(x - b) >= abs(x - a):
        stdout.write("A")
        a = x
    else:
        stdout.write("B")
        b = x
