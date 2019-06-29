
n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
max_arr = arr[n-1]
x,y = 1,2
for i in range(n-1, 0, -1):
    arr[i] += arr[i+1]
    new = arr[i] - arr[n-x]
    if new > max_arr:
        max_arr = new
    b = x+1
    if b==y:
        x = 0
        y+=1
print(max_arr)
