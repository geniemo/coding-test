H, W, N, M = map(int, input().split())

a = 1 + (H - 1) // (N + 1)
b = 1 + (W - 1) // (M + 1)

print(a * b)
