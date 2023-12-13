import re


def solve_1(lines):
    result = 0
    for line in lines:
        parts = line.split()
        ns = [int(s) for s in parts[1].split(',')]
        # result += nb_possible(parts[0], ns)
        result += count_2(parts[0], ns)
    return result


"""
Si je sais résoudre s, ns est-ce que je sais résoudre :
- s+'#',ns
- s+'.',ns
- s+'?',ns

il y a entre 9 et 29 intervales d'au moins un '.' entre les '#',
avec possibilité d'ajouter des points sur les côtés ou pas à chaque fois.
plan
- choisir un pivot dans les dominos à insérer,
- compacter les dominos à gauche et à droite
- compter combien de possibilité on a d'insérer le pivot
- multiplier la valeur de chaque pivot (assert qu'aucune n'est zéro)
- pb : les # déjà placés peuvent compliquer la tâche de compactage ?
"""
def solve_2(lines):
    result = 0
    for line in lines:
        parts = line.split()
        s =  '?'.join([parts[0]]*5)
        ns = [int(s) for s in parts[1].split(',')]*5
        result += count_2(s, ns)


def count_2(s, ns):
    print(s)
    print(ns)
    nb_ns = len(ns)
    result_line = 1
    for i in range(nb_ns):
        nb_left = i
        nb_right = nb_ns - i -1
        left = compact_left(s, ns[:i])
        right = compact_right(s, ns[i+1:])
        sub = s[left:right]
        nb_pos = nb_possible(sub, [ns[i]])
        if nb_pos > 0:
            result_line *= nb_pos
    print(result_line)
    print()
    return result_line


def compact_left(s, ns):
    start, end = 0, 0

    result = ''
    for n in ns:
        while True:
            c = s[end]
            if c in '?#':
                end += 1
            else:
                start += 1
                end = start
            if n <= abs(end - start):
                end += 1
                start = end
                break

    return end


def compact_right(s, ns):
    end, start = len(s)-1, len(s)-1

    result = ''
    for n in reversed(ns):
        while True:
            assert end > 0
            c = s[end]
            if c in '?#':
                end += -1
            else:
                start += -1
                end = start
            if n <= abs(end - start):
                end += -1
                start = end
                break

    return end+1


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


# string, begin, width
def next_slot(s, b, w):
    start = b
    end = b+w
    while True:
        if all(c in '?#' for c in s[start:end]):
            break
        start += 1
        end += 1
    while s[end] == '#':
        end += 1
    return end+1


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
# print(solve_2(lines))

##
# Tests
assert 2 == next_slot('???.###', 0, 1)
assert 4 == next_slot('???.###', 2, 1)
assert 3 == next_slot('.??.###', 0, 1)
assert 5 == next_slot('?###..', 0, 3)
