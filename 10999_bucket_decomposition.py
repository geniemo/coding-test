import sys
import math


def input():
    return sys.stdin.readline().strip()


n, m, k = map(int, input().split())
n_arr = [int(input()) for _ in range(n)]
b_size = int(math.sqrt(n))
b_arr = [sum(n_arr[i : min(n, i + b_size)]) for i in range(0, n, b_size)]
b_buf = [0] * len(b_arr)


def add(b, c, d):
    global n, m, k, n_arr, b_size, b_arr

    idx, en = b - 1, c - 1
    while idx <= en:
        b_idx = idx // b_size
        # 이 반복에서의 버킷이 범위에 전부 포함되어 있을 때
        if idx % b_size == 0 and idx + b_size - 1 <= en:
            # n이 크고 b, c가 전체 범위라면 TLE -> lazy 적용
            # for i in range(idx, idx + b_size):
            #     n_arr[i] += d

            # 실제로 값을 업데이트하지 않고, 해당 버킷의 각 요소에 더해줘야 하는 값만 따로 보관
            b_buf[b_idx] += d
            idx += b_size
        # 버킷이 범위에 부분적으로만 포함되어 있을 때
        else:
            n_arr[idx] += d
            b_arr[b_idx] += d
            idx += 1


def query(b, c):
    global n, m, k, n_arr, b_size, b_arr

    result = 0
    idx, en = b - 1, c - 1
    while idx <= en:
        b_idx = idx // b_size
        # 이 반복에서의 버킷이 범위에 전부 포함되어 있을 때
        if idx % b_size == 0 and idx + b_size - 1 <= en:
            result += b_arr[b_idx] + b_buf[b_idx] * b_size
            idx += b_size
        # 버킷이 범위에 부분적으로만 포함되어 있을 때
        else:
            result += n_arr[idx] + b_buf[b_idx]
            idx += 1
    return result


for _ in range(m + k):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        add(*cmd[1:])
    else:
        print(query(*cmd[1:]))
