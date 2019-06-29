l = [0, 0, 0, 0, 0]
for j in range(5, 100001):
    bin_n = bin(j)[2:]
    str_bin = str(bin_n)
    len_str = len(str_bin)
    count = 0
    for i in range(0, len_str, 1):
        if i + 1 >= (len_str - 1):
            break
        if str_bin[i] == '1' and str_bin[i + 1] == '0' and str_bin[i + 2] == '1':
            count += 1

    l.append(count)

print(l)
print(len(l))

for _ in range(int(input())):
    r, k = map(int, input().split())
    very_cool = 0
    for i in range(5, r + 1, 1):
        coolness = l[i]
        if coolness >= k:
            very_cool += 1
    print(very_cool)