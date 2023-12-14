from collections import defaultdict


def solve_1(lines):
    grid = build_empty_grid(lines)
    tilted = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'O':
                fall(grid, i, j)
    result = 0
    w = len(lines[0])
    for i, line in enumerate(lines):
        for j in range(w):
            if grid[i, j] == 'O':
                result += w-i
    return result


def build_empty_grid(lines):
    grid = defaultdict(lambda: '#')
    w = len(lines[0])
    h = len(lines)
    for i in range(h):
        line = lines[i]
        for j in range(w):
            c = line[j]
            if c == 'O':
                grid[i, j] = '.'
            else:
                grid[i,j] = c
    return grid


def fall(grid, i, j):
    below = i
    while grid[below, j] == '.':
        below -= 1
    grid[below+1, j] = 'O'


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
text = open(0).read()
lines = text.split('\n')[:-1]
print(solve_1(lines))
