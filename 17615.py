N = int(input())
balls = input()

if "R" not in balls or "B" not in balls:
    print(0)
    exit(0)

# 가장 오른쪽에 있는 공과 같은 공들을 오른쪽으로 다 모으는 경우
last_ball = balls[-1]
other_ball = "B" if last_ball == "R" else "R"
idx = balls.rfind(other_ball)
m = balls[:idx + 1].count(last_ball)

# 가장 왼쪽에 있는 공과 같은 공들을 왼쪽으로 다 모으는 경우
first_ball = balls[0]
other_ball = "B" if first_ball == "R" else "R"
idx = balls.find(other_ball)
m = min(m, balls[idx:].count(first_ball))


# 양 끝단의 공이 같은 공일 때, 사이에 있는 다른 공을 한 쪽으로 모으는 경우
if first_ball == last_ball:
    m = min(m, balls.count(other_ball))

print(m)