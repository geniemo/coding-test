from collections import deque, defaultdict

s = input()
t = input()
q = deque([s])
visited = defaultdict(lambda: False)

while len(q) > 0:
    cur = q.popleft()
    if cur == t:
        print(1)
        exit()

    if visited[cur]:
        continue
    visited[cur] = True

    for nxt in (cur + "A", (cur + "B")[::-1]):
        if len(nxt) <= 50 and not visited[nxt] and (cur in t or cur[::-1] in t):
            q.append(nxt)
print(0)
