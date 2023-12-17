from collections import deque


def solve_1(matrix):
    w = len(matrix[0])
    h = len(matrix)
    start_1 = ((0, 0, 0, 1, 0), 0)  # ((i, j, di, dj, n), h)
    start_2 = ((0, 0, 1, 0, 0), 0)  # ((i, j, di, dj, n), h)
    seen = {start_1: 99999, start_2: 9999999}
    q = deque([start_1, start_2])
    while q:
        node, heat = q.popleft()
        for n in neighbors(w, h, node):
            ni = n[0]
            nj = n[1]
            new_heat = heat + matrix[ni][nj]
            if n not in seen or (n in seen and new_heat < seen[n]):
                seen[n] = new_heat
                q.append((n, new_heat))
    result = 99999
    for k, v in seen.items():
        if k[0] == h-1 and k[1] == w-1:
            result = min(result, v)
    return result


def neighbors(w, h, node):
    i, j, di, dj, n = node
    result = []
    if n < 3 and is_in(w, h, i+di, j+dj):
        result.append((i+di, j+dj, di, dj, n+1))
    left_di, left_dj = left(di, dj)
    left_i = i+left_di
    left_j = j+left_dj
    if is_in(w, h, left_i, left_j):
        result.append((left_i, left_j, left_di, left_dj, 1))
    right_di, right_dj = right(di, dj)
    right_i = i+right_di
    right_j = j+right_dj
    if is_in(w, h, right_i, right_j):
        result.append((right_i, right_j, right_di, right_dj, 1))
    return result


def is_in(w, h, i, j):
    return (0 <= i < h) and (0 <= j < w)


def left(di, dj):
    assert 0 == di or 0 == dj
    if di == 0:
        return (-1, 0) if dj == 1 else (1, 0)
    else:
        return (0, 1) if di == 1 else (0, -1)

assert (-1, 0) == left(0, 1)
assert (1, 0) == left(0, -1)
assert (0, 1) == left(1, 0)
assert (0, -1) == left(-1, 0)

def right(di, dj):
    if di == 0:
        return (1, 0) if dj == 1 else (-1, 0)
    else:
        return (0, -1) if di == 1 else (0, 1)

assert (1, 0) == right(0, 1)
assert (-1, 0) == right(0, -1)
assert (0, -1) == right(1, 0)
assert (0, 1) == right(-1, 0)


ex = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
text = ex
# text = open(0).read()
numbers = [[int(c) for c in line] for line in text.splitlines()]
print(solve_1(numbers))
