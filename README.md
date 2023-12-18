Advent of [bad] Code, 2023 edition

- <https://adventofcode.com>

## Learnings

To compute the area of a polygon defined by the closed points sequence {(x<sub>i</sub>, y<sub>i</sub>)}, just take the sum of all the "oriented" trapezoid areas, 1/2\*(y<sub>i</sub>+y<sub>i+1</sub>)\*(x<sub>i</sub>-x<sub>i+1</sub>) (positive in one direction, negative in the other):
- <https://en.wikipedia.org/wiki/Shoelace_formula#Trapezoid_formula_2>
