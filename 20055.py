import sys
from collections import deque
from dataclasses import dataclass


def input():
    return sys.stdin.readline().strip()


N, K = map(int, input().split())


@dataclass
class block:
    durability: int
    is_loaded: bool


blocks = deque(block(durability, False) for durability in map(int, input().split()))


def getoff():
    if blocks[N - 1].is_loaded:
        blocks[N - 1].is_loaded = False


def rotate():
    blocks.appendleft(blocks.pop())
    getoff()


def move():
    # 가장 먼저 올라간 로봇부터
    for i in range(N - 2, 0, -1):
        # 현재 칸에 로봇이 있고 다음 칸에 로봇이 없고 내구도가 1 이상이면 이동
        if (
            blocks[i].is_loaded == True
            and blocks[i + 1].is_loaded == False
            and blocks[i + 1].durability >= 1
        ):
            blocks[i].is_loaded = False
            blocks[i + 1].is_loaded = True
            blocks[i + 1].durability -= 1
    getoff()


def load():
    if blocks[0].is_loaded == False and blocks[0].durability >= 1:
        blocks[0].is_loaded = True
        blocks[0].durability -= 1


def is_finished():
    return len(list(filter(lambda b: b.durability == 0, blocks))) >= K


result = 0
while not is_finished():
    rotate()
    move()
    load()
    result += 1
print(result)
