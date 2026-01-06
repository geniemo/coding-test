from dataclasses import dataclass
import sys

rl = sys.stdin.readline

N, K = map(int, rl().split())


@dataclass
class Country:
    id: int
    gold: int
    silver: int
    bronze: int


def is_c1_win(c1, c2):
    result = False
    if c1.gold > c2.gold:
        result = True
    elif c1.gold == c2.gold:
        if c1.silver > c2.silver:
            result = True
        elif c1.silver == c2.silver:
            if c1.bronze > c2.bronze:
                result = True
    return result


countries = []
target_country = None
for i in range(N):
    countries.append(Country(*map(int, rl().split())))
    if countries[i].id == K:
        target_country = countries[i]


count = 0
for c in countries:
    if is_c1_win(c, target_country):
        count += 1

print(count + 1)
