import sys

M = int(sys.stdin.readline())
S = set()
all_set = {i for i in range(1, 21)}

for _ in range(M):
    cmd = sys.stdin.readline()
    try:
        func, x = cmd.split()
        x = int(x)
    except Exception:
        func = cmd.strip()

    if func == "add":
        S.add(x)
    elif func == "remove":
        if x in S:
            S.remove(x)
    elif func == "check":
        print(int(x in S))
    elif func == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif func == "all":
        S = all_set.copy()
    elif func == "empty":
        S.clear()
