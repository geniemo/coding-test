import sys


def input():
    return sys.stdin.readline().strip()


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * 4 * n
lazy = [0] * 4 * n


def build(node, st, en):
    global n, m, k, arr, tree, lazy
    if st == en:
        tree[node] = arr[st]
    else:
        mid = (st + en) // 2
        build(node * 2, st, mid)
        build(node * 2 + 1, mid + 1, en)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def propagate(node, st, en):
    global n, m, k, arr, tree, lazy
    tree[node] += lazy[node] * (en - st + 1)
    # 자식이 있으면 자식에게 lazy 전파
    if st != en:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0


def update(node, st, en, l, r, val):
    global n, m, k, arr, tree, lazy
    propagate(node, st, en)
    if r < st or en < l:
        return
    if l <= st and en <= r:
        lazy[node] += val
        propagate(node, st, en)
        return
    mid = (st + en) // 2
    update(node * 2, st, mid, l, r, val)
    update(node * 2 + 1, mid + 1, en, l, r, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, st, en, l, r):
    global n, m, k, arr, tree, lazy
    propagate(node, st, en)
    if r < st or en < l:
        return 0
    if l <= st and en <= r:
        return tree[node]
    mid = (st + en) // 2
    return query(node * 2, st, mid, l, r) + query(node * 2 + 1, mid + 1, en, l, r)


build(1, 0, n - 1)

for _ in range(m + k):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        _, b, c, d = cmd
        update(1, 0, n - 1, b - 1, c - 1, d)
    else:
        _, b, c = cmd
        print(query(1, 0, n - 1, b - 1, c - 1))
