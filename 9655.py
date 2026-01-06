N = int(input())

"""
한 턴에 2, 4, 6

2 - a b
3 - a b a
4 - aaa b
5 - a bbb a
6 - aaa b a b
7 - a bbb a b a

이는 조건
1. 1개일 때 내차례
2. 5개일 때 내차례

N개일 때 내차례를 만들려면 N + 4개 때 내차례여야 한다

따라서 홀수일 때만 내가 이김
"""

if N % 2 != 0:
    print("SK")
else:
    print("CY")
