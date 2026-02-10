import sys
import math


def input():
    return sys.stdin.readline().strip()


n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()


def is_possible(mid):
    """
    공유기 간 거리의 최소가 mid일 때 배치가 가능한가
    """
    global n, c, x
    cur = -math.inf
    cnt = 0
    for _x in x:
        d = _x - cur
        if d >= mid:
            cnt += 1
            cur = _x
    return cnt >= c


lo, hi = 1, 10_0000_0000
while lo < hi:
    mid = (lo + hi + 1) // 2
    if is_possible(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
