import sys

rl = sys.stdin.readline

P = int(rl().strip())
for _ in range(P):
    line = list(map(int, rl().split()))
    t = line.pop(0)

    step_count = 0
    sorted_line = [line.pop(0)]
    while len(line) > 0:
        cur = line.pop(0)
        idx = len(sorted_line)
        for i, h in enumerate(sorted_line):
            if h > cur:
                idx = i
                break
        step_count += len(sorted_line) - idx
        sorted_line.insert(idx, cur)
    print(t, step_count)
