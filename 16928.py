import sys
from math import inf
from collections import deque


def input():
    return sys.stdin.readline().strip()


board = [inf for _ in range(101)]
move = [i for i in range(101)]

N, M = map(int, input().split())
for _ in range(N + M):
    f, t = map(int, input().split())
    move[f] = t

q = deque([1])
board[1] = 0
while len(q) > 0:
    cur = q.popleft()
    # 주사위 1~6
    for nxt in range(cur + 1, min(cur + 7, 101)):
        # 사다리/뱀 이동, 없는 경우 제자리
        nxt = move[nxt]
        if board[nxt] > board[cur] + 1:
            board[nxt] = board[cur] + 1
            q.append(nxt)
print(board[100])
