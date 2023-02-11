n, m = [int(x) for x in input().split()]
f = sorted([int(x) for x in input().split()])
t = sorted([int(x) for x in input().split()])
ans = 0
i = 0
j = 0
while j < len(t) and i < len(f):
    if t[j] > f[i]:
        j+=1
        i+=1
        ans+=1
    else:
        j+=1
print(ans)
