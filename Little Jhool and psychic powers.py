

from sys import stdin, stdout

string = stdin.readline()
c = False
for i in range(len(string)):
    if i + 5 > len(string):
        break
    if string[i] != string[i + 1] and string[i] != string[i + 2] and string[i] != string[i + 3] and string[i] != string[
        i + 4] and string[i] != string[i + 5]:
        c = True
    else:
        c = False
    if string.count('0')>=string.count('1') or string.count('1')>=string.count('0'):
        c=True

if c:
    stdout.write("Good luck!")
else:
    stdout.write("Sorry, sorry!")