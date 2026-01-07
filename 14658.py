import sys


def input():
    return sys.stdin.readline().strip()


N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

xs = set([x for x, _ in stars])
ys = set([y for _, y in stars])


def count_stars(xl, xr, yd, yu):
    cnt = 0
    for x, y in stars:
        if xl <= x <= xr and yd <= y <= yu:
            cnt += 1
    return cnt


_max = 0
for x in xs:
    for y in ys:
        _max = max(_max, count_stars(x, x + L, y, y + L))
print(K - _max)
