N = int(input())

channels = []
for _ in range(N):
    channels.append(input())

answer = ""
kbs1 = channels.index("KBS1")
answer += "1" * kbs1 + "4" * kbs1
channels.remove("KBS1")
channels.insert(0, "KBS1")

kbs2 = channels.index("KBS2")
answer += "1" * kbs2 + "4" * (kbs2 - 1)

print(answer)
