Advent of [bad] Code, 2023 edition

- <https://adventofcode.com>

## Learnings

To compute the area of a polygon defined by the closed points sequence {(x<sub>i</sub>, y<sub>i</sub>)}, just take the sum of all the "oriented" trapezoid areas, 1/2\*(y<sub>i</sub>+y<sub>i+1</sub>)\*(x<sub>i</sub>-x<sub>i+1</sub>) (positive in one direction, negative in the other):
- <https://en.wikipedia.org/wiki/Shoelace_formula#Trapezoid_formula_2>

For day 18, we could imagine that the polygon resulting from all the 90 degrees
turns was centered in the cubes. Then, we can add `(d1 ∧ d2)(d2 - d1)/2` to
each point of the polygon to compute an envelope of the right size. d1 and d2
are the normalized directions of the edges that meet at each point. Then, the
above trapezoid formula works out of the box. This idea allows to grow the
"padding" further, by changing the 1/2 factor.
