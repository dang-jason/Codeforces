n, m = [int(x) for x in input().split()]
e = [int(x) for x in input().split()]
i = 0
ans = 0
cur = 1
while i < len(e):
    eneed = 0
    for _ in range(m):
        eneed += cur
        cur += 1
    while eneed > 0 and i < len(e):
        eneed -= e[i]
        i += 1
    if eneed <= 0:
        ans += 1
print(ans)