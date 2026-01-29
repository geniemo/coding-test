import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


N = int(input())
options = [input().split() for _ in range(N)]
hotkeys = set()

for word_list in options:
    # 단어 기준으로 단축키 등록
    hotkey_enrolled = False
    for i, w in enumerate(word_list):
        first_char = w[0].lower()
        if first_char not in hotkeys:
            hotkeys.add(first_char)
            hotkey_enrolled = True
            word_list[i] = f"[{w[0]}]{w[1:]}"
            break
    if hotkey_enrolled:
        continue
    # 문자 기준으로 단축키 등록
    for i, w in enumerate(word_list):
        for j, c in enumerate(map(str.lower, w)):
            if c not in hotkeys:
                hotkeys.add(c)
                hotkey_enrolled = True
                word_list[i] = f"{w[:j]}[{w[j]}]{w[j + 1:]}"
                break
        if hotkey_enrolled:
            break

for word_list in options:
    print(" ".join(word_list))
