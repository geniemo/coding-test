import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


N, M = map(int, input().split())
roads = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    roads[A].append((B, C))  # A -> B, 여물은 C
    roads[B].append((A, C))  # B -> A, 여물은 C

pq = [(0, 1)]
heapq.heapify(pq)
visited = defaultdict(lambda: 0x7F7F7F7F)

visited[1] = 0
while pq:
    food, cur = heapq.heappop(pq)
    if visited[cur] < food:
        continue
    for to, cost in roads[cur]:
        nfood = food + cost
        if nfood < visited[to]:
            heapq.heappush(pq, (nfood, to))
            visited[to] = nfood
print(visited[N])
