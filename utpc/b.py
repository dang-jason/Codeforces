n = int(input())
num = [int(x) for x in str(n)]
x = 0
for i in num:
    x += i
water = 0
for i in range(7):
    water += n
    n += x
print(water)