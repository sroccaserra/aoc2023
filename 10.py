from collections import defaultdict, deque


def solve_1(grid):
    start = None
    for k, v in grid.items():
        if v == 'S':
            start = k
            break
    dists = {start: 0}
    q = deque([start])
    result = 0
    while q:
        pos = q.popleft()
        d = dists[pos]
        for n in neighbors(grid, pos):
            if n in dists:
                continue
            q.append(n)
            dists[n] = d+1
            result = max(result, d+1)
    return result


def neighbors(grid, pos):
    i, j = pos
    result = []
    c = grid[(i, j)]
    if c in 'S-FL' and grid[(i, j+1)] in '-J7':
        result.append((i, j+1))
    if c in 'S7J-' and grid[(i, j-1)] in 'FL-':
        result.append((i, j-1))
    if c in 'SF7|' and grid[(i+1, j)] in 'JL|':
        result.append((i+1, j))
    if c in 'SLJ|' and grid[(i-1, j)] in 'F7|':
        result.append((i-1, j))
    return result


ex = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""
text = ex
# text = open(0).read()
lines = text.split('\n')[:-1]
grid = defaultdict(lambda: '.')
w = len(lines[0])
h = len(lines)
for i in range(h):
    line = lines[i]
    for j in range(w):
        grid[(i, j)] = line[j]
print(solve_1(grid))
