from collections import defaultdict


def solve_1(lines):
    grid = build_grid(lines)
    w = len(lines[0])
    h = len(lines)
    for i in range(h):
        for j in range(w):
            if grid[i, j] == 'O':
                fall(grid, -1, 0, i, j)
    result = 0
    for i in range(h):
        for j in range(w):
            if grid[i, j] == 'O':
                result += w-i
    return result


def build_grid(lines):
    grid = defaultdict(lambda: '#')
    w = len(lines[0])
    h = len(lines)
    for i in range(h):
        line = lines[i]
        for j in range(w):
            grid[i,j] = line[j]
    return grid


def fall(grid, vec_i, vec_j, i, j):
    grid[i,j] = '.'
    while grid[i+vec_i, j+vec_j] == '.':
        i += vec_i
        j += vec_j
    grid[i, j] = 'O'


ex = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
text = ex
# text = open(0).read()
lines = text.split('\n')[:-1]
print(solve_1(lines))
