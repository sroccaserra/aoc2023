def solve_1(patterns):
    result_h = 0
    result_v = 0
    for p in patterns:
        result_h += count_horizontal(p)
        w = len(p[0])
        h = len(p)
        transposed = []
        for j in range(w):
            row = []
            transposed.append(row)
            for i in range(h):
                row.append(p[i][j])
        result_v += count_horizontal(transposed)

    return result_h*100+result_v

def solve_2(patterns):
    result_h = 0
    result_v = 0
    for p in patterns:
        result_h += find_with_diff_of_one(p)
        w = len(p[0])
        h = len(p)
        transposed = []
        for j in range(w):
            row = []
            transposed.append(row)
            for i in range(h):
                row.append(p[i][j])
        result_v += find_with_diff_of_one(transposed)

    return result_h*100+result_v

def count_horizontal(p):
    n = 0
    for n in range(len(p)-1):
        a = min(n+1, len(p)-n-1)
        start = n+1-a
        end = n+1+a
        sub = p[start:end]
        if sub == list(reversed(sub)):
            return n+1
    return 0

def find_with_diff_of_one(p):
    n = 0
    for n in range(len(p)-1):
        a = min(n+1, len(p)-n-1)
        start = n+1-a
        end = n+1+a
        sub = p[start:end]
        w = len(sub[0])
        i = 0
        diff = 0
        for line_r in reversed(sub):
            line = sub[i]
            for j in range(w):
                if line[j] != line_r[j]:
                    diff += 1
            i += 1
        if diff == 2:
            return n+1
    return 0

ex = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
text = ex
# text = open(0).read()
patterns = [lines.split('\n') for lines in text[:-1].split('\n\n')]
print(solve_1(patterns))
print(solve_2(patterns))
