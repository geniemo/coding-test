from collections import deque

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def chunk(visited, x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    result = [(x, y)]
    s = countries[x][y]
    while len(q) > 0:
        x, y = q.popleft()
        for _dx, _dy in zip(dx, dy):
            nx = x + _dx
            ny = y + _dy
            if (
                (0 <= nx < N and 0 <= ny < N)
                and (not visited[nx][ny])
                and (L <= abs(countries[x][y] - countries[nx][ny]) <= R)
            ):
                q.append((nx, ny))
                visited[nx][ny] = True
                result.append((nx, ny))
                s += countries[nx][ny]
    mean = s // len(result)
    for x, y in result:
        countries[x][y] = mean
    return len(result) > 1


def population_move():
    is_moved = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                _is_moved = chunk(visited, i, j)
                if not is_moved:
                    is_moved = _is_moved
    return is_moved


days = 0
while population_move():
    days += 1
print(days)
