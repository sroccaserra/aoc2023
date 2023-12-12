import re


def solve_1(lines):
    result = 0
    for line in lines:
        parts = line.split()
        ns = [int(s) for s in parts[1].split(',')]
        result += nb_possible(parts[0], ns)
    return result


def nb_possible(s, ns):
    nb_qs = len([c for c in s if c =='?'])
    result = 0
    for i in range(2**nb_qs):
        cs = ''
        n_q = 0
        for j, c in enumerate(s):
            if c == '?':
                if 1 == 1&(i>>n_q):
                    cs += '#'
                else:
                    cs += '.'
                n_q += 1
            else:
                cs += c
        if ns == [len(w) for w in cs.split('.') if w != '']:
            result += 1
    return result


ex = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
text = ex
# text = open(0).read()
lines = text.split('\n')[:-1]
print(solve_1(lines))
