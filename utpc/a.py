ans = 0
num = [float(num) for num in input().split()]
for i in range(28):
    if num[i] >= .8:
        ans += 1
print(ans)