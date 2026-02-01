import sys


def input():
    return sys.stdin.readline().strip()


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
for y in range(H):
    before = None
    for x in range(W):
        if blocks[x] > y:
            if before is not None:
                water += x - before - 1
            before = x
print(water)
