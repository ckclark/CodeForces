n, x0 = map(int, raw_input().split())
l, r = 0, 1000
for i in range(n):
    ai, bi = map(int, raw_input().split())
    ai, bi = min(ai, bi), max(ai, bi)
    l = max(ai, l)
    r = min(bi, r)
if l > r:
    print -1
elif l <= x0 <= r:
    print 0
else:
    print min(abs(r - x0), abs(x0 - l))

