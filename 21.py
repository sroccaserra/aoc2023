from collections import defaultdict, deque


Pos = tuple[int, int]
Dist = int


def solve_1(lines, max_steps=6):
    w = len(lines[0])
    h = len(lines)
    start_pos = (-1, -1)
    grid = defaultdict(lambda: '#')
    for i in range(h):
        line = lines[i]
        for j in range(w):
            c = line[j]
            if c == 'S':
                start_pos = (i, j)
            grid[i, j] = line[j]
    q:deque[tuple[Pos, Dist]] = deque([(start_pos, 0)])
    seen:set[tuple[Pos, Dist]] = set([(start_pos, 0)])
    dests:set[Pos] = set()
    while q:
        pos, dist = q.popleft()
        for next_pos in neighbors_1(grid, pos):
            next_dist = dist + 1
            next_node = (next_pos, next_dist)
            if next_node in seen:
                continue
            if next_dist < max_steps:
                q.append(next_node)
                seen.add(next_node)
            elif next_dist == max_steps:
                dests.add(next_pos)
            else: assert False
    return len(dests)


def solve_2(lines, max_steps=6):
    w = len(lines[0])
    h = len(lines)
    start_pos = (-1, -1)
    for i in range(h):
        line = lines[i]
        for j in range(w):
            c = line[j]
            if c == 'S':
                start_pos = (i, j)
    q:deque[tuple[Pos, Dist]] = deque([(start_pos, 0)])
    seen:set[tuple[Pos, Dist]] = set([(start_pos, 0)])
    dests:set[Pos] = set()
    while q:
        pos, dist = q.popleft()
        for next_pos in neighbors_2(lines, w, h, pos):
            next_dist = dist + 1
            next_node = (next_pos, next_dist)
            if next_node in seen:
                continue
            if next_dist < max_steps:
                q.append(next_node)
                seen.add(next_node)
            elif next_dist == max_steps:
                dests.add(next_pos)
            else: assert False
    return len(dests)


def neighbors_1(grid, pos):
    i, j = pos
    result = []
    for n in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if grid[n] != '#':
            result.append(n)
    return result


def neighbors_2(lines, w, h, pos):
    i, j = pos
    result = []
    for n_i, n_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if lines[n_i%h][n_j%w] != '#':
            result.append((n_i, n_j))
    return result


ex = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''
text = ex
# text = open(0).read()
lines = text.splitlines()
print(solve_1(lines, 6))
# print(solve_1(lines, 64))
print(solve_2(lines, 100))
