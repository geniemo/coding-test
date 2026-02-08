import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edges.append(tuple(map(int, input().split())))

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[b] > rank[a]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


edges.sort(key=lambda e: e[2])
result = 0
for e in edges:
    a, b, c = e
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)
