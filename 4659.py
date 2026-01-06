import sys

rl = sys.stdin.readline


def is_vowel(c):
    return c in "aeiou"


while True:
    pw = rl().strip()

    conso_cnt = 0
    vowel_cnt = 0

    if pw == "end":
        break

    # 모음 포함 여부
    if not ("a" in pw or "e" in pw or "i" in pw or "o" in pw or "u" in pw):
        print(f"<{pw}> is not acceptable.")
        continue

    is_acceptable = True
    for i in range(len(pw)):
        # 자음 또는 모음 연속 3개 체크
        if is_vowel(pw[i]):
            conso_cnt = 0
            vowel_cnt += 1
        else:
            vowel_cnt = 0
            conso_cnt += 1

        if conso_cnt >= 3 or vowel_cnt >= 3:
            is_acceptable = False
            break

        # 같은 글자 연속 두번 체크
        if i >= 1 and pw[i] == pw[i - 1] and pw[i] not in "eo":
            is_acceptable = False
            break

    if is_acceptable:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
