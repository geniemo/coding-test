import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

uniques = defaultdict(int)
for i in range(k):
    uniques[sushi[i]] += 1
uniques[c] += 1

M = len(uniques)
for i in range(k, len(sushi) + k - 1):
    i %= N
    # 가장 오래된 것 빼기
    uniques[sushi[i - k]] -= 1
    if uniques[sushi[i - k]] == 0:
        del uniques[sushi[i - k]]

    # 새로운 스시 추가
    uniques[sushi[i]] += 1

    # 최댓값 갱신
    M = max(M, len(uniques))

print(M)
