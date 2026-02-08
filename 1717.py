import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        # rank 가 더 큰 트리에 작은 트리를 붙인다
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    elif c == 1:
        print("YES" if find(a) == find(b) else "NO")
