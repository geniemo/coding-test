import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


# 어떤 문자 c를 K개 포함하는 가장 짧은 연속 문자열은 시작도 c, 끝도 c이다.
# 어떤 문자 c를 K개 포함하고, 첫, 마지막 글자가 같은 가장 긴 연속 문자열은 그 사이에 c가 K - 2 개 있다.
def sol():
    shortest = 0x7F7F7F7F
    longest = -0x7F7F7F7F
    for c in alphabets:
        for i in range(len(pos[c]) - K + 1):
            l, r = i, i + K - 1
            shortest = min(shortest, pos[c][r] - pos[c][l] + 1)
            longest = max(longest, pos[c][r] - pos[c][l] + 1)
    return shortest, longest


T = int(input())
alphabets = [chr(97 + i) for i in range(26)]
for _ in range(T):
    W = input()
    K = int(input())
    pos = defaultdict(list)
    for i, c in enumerate(W):
        pos[c].append(i)
    # K개 이상 등장하는 문자가 없다면 -1
    if max(map(lambda p: len(p), pos.values())) < K:
        print(-1)
        continue
    print(*sol())
