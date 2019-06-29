
x,y = zip(*(map(int, input().split()) for _ in range(int(input()))))
x = list(x)
y = list(y)
x.sort()
y.sort()
main_index = len(x) // 2
sum_x = 0
sum_y = 0
for i,j in zip(x,y):
    sum_x += abs(x[main_index] - i)
    sum_y += abs(y[main_index] - j)

print(min(sum_x, sum_y))
