x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

distance = (x3-x1)**2 + (y3-y1)**2
r1 = (x2-x1)**2 + (y2-y1)**2
r2 = (x4-x3)**2 + (y4-y3)**2
print(distance, r1, r2)
if r1+r2 >= distance:
    print("Yes")
else:
    print("No")