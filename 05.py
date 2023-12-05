def solve_1(parts):
    ns = [int(s) for s in parts[0][0][7:].split()]
    rest = parts[1:]
    maps = [parse_maps(inst) for inst in rest]
    return min([convert(maps, n) for n in ns])


def parse_maps(map_struct):
    header_line = map_struct[0]
    header_parts = header_line.split('-to-')
    header = (header_parts[0][:2], header_parts[1][:2])

    map_lines = map_struct[1:]
    range_specs = [[int(s) for s in line.split()] for line in map_lines]
    return header, [(spec[1], spec[1]+spec[2]-1, spec[0]-spec[1])for spec in range_specs]


def convert(maps, value):
    result = value
    for m in maps:
        buckets = m[1]
        for s, e, i in buckets:
            if s <= result <= e:
                result += i
                break
    return result


ex = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

text = ex[:-1]
text = open(0).read()[:-1]
parts = [par.split('\n') for par in text.split('\n\n')]

print(solve_1(parts))
