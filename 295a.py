n, m, k = [int(init) for init in input().split()]
a = [int(init) for init in input().split()]

oper = []
for _ in range(m):
	l, r, d = input().split()
	oper.append([int(l)-1, int(r), int(d)])

q = [0]*len(oper)
for _ in range(k):
	x, y = input().split()
	x, y = int(x)-1, int(y)
	q[x] += 1
	if y in range(len(q)):
		q[y] -= 1

adder = [0]*len(a)
csum = 0
for i in range(len(q)):
	csum += q[i]
	l, r, d = oper[i]
	adder[l] += d*csum
	if r in range(len(adder)):
		adder[r] -= d*csum

csum = 0
for r in range(len(adder)):
	csum += adder[r]
	a[r] += csum

print(*a)