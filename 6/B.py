n, m, c = raw_input().split()
n, m = int(n), int(m)
room = []
deputy = set()
for i in range(n):
    room.append(raw_input())
for i in range(n):
    for j in range(m):
        if room[i][j] == c:
            if i > 0:
                deputy.add(room[i - 1][j])
            if i < n - 1:
                deputy.add(room[i + 1][j])
            if j > 0:
                deputy.add(room[i][j - 1])
            if j < m - 1:
                deputy.add(room[i][j + 1])

print len([x for x in deputy if x != c and x != '.'])
