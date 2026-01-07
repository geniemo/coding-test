from math import inf
from collections import deque


N, K = map(int, input().split())

q = deque([N])
record = [inf for _ in range(100001)]
record[N] = 0
while True:
    cur = q.popleft()
    if cur == K:
        print(record[K])
        break

    nxt = cur * 2
    while nxt <= 100000:
        if record[nxt] > record[cur]:
            record[nxt] = record[cur]
            q.appendleft(nxt)
            nxt *= 2
        else:
            break

    nxt = cur + 1
    if nxt <= 100000 and record[nxt] > record[cur] + 1:
        record[nxt] = record[cur] + 1
        q.append(nxt)

    nxt = cur - 1
    if nxt >= 0 and record[nxt] > record[cur] + 1:
        record[nxt] = record[cur] + 1
        q.append(nxt)
