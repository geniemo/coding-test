import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = defaultdict(int)
l, r = 0, 0

maximum = -1
while r < N:
    # r번째 숫자 카운트 추가
    cnt[arr[r]] += 1
    # 새로 추가된 숫자 카운트가 K를 초과한다면 l을 오른쪽으로 이동시키면서 카운트 마이너스
    while cnt[arr[r]] > K:
        cnt[arr[l]] -= 1
        l += 1
    maximum = max(maximum, r - l + 1)

    # r 오른쪽으로 이동
    r += 1
print(maximum)
