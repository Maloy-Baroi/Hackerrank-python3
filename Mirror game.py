
vowel = {'A', 'E', 'I', 'O', 'U'}
s = input()
stuart = 0
kevin = 0
to_kevin = ''
to_stuart = ''
for i in s:
    if i not in vowel:
        to_stuart += i
        stuart += s.count(to_stuart)
    else:
        to_kevin += i
        kevin += s.count(to_kevin)

print(stuart)
print(kevin)