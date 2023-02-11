n, k = [int(x) for x in input().split()]
ans = 0
if k != 0:
    for r in range(1,n+1):
        if r*k > n:
            break
        if r*k+r <= n:
            ans += ((r*k+r) - (r*k)) 
        else: 
            ans += n+1 - (r*k)
else:
    ans = n(n-1)/2
print(ans)

