import sys
from dataclasses import dataclass
from collections import deque


def input():
    return sys.stdin.readline().strip()


@dataclass
class Road:
    fr: int
    to: int
    length: int


N, D = map(int, input().split())
roads = [Road(*map(int, input().split())) for _ in range(N)]
dq = deque()
dq.append((0, 0))
minimum = D
while len(dq) > 0:
    cur = dq.popleft()
    minimum = min(minimum, cur[1] + D - cur[0])
    # 현재 위치에서 탈 수 있는 모든 지름길 순회
    available_roads = list(
        filter(lambda r: r.fr >= cur[0] and r.fr < D and r.to <= D, roads)
    )
    for road in available_roads:
        # 그 지름길의 목적지까지 운전한 거리
        length = cur[1] + road.fr - cur[0] + road.length
        dq.append((road.to, length))
print(minimum)
