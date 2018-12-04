from collections import namedtuple
from itertools import combinations

claims = {}
for line in open('input.txt'):
    spl_line = line.split()
    value_list = [spl_line[2][:-1].split(','), spl_line[3].split('x')]
    value_list[0] = list(map(int, value_list[0]))
    value_list[1] = list(map(int, value_list[1]))
    claims[spl_line[0][1:]] = value_list

no_collision = set(claims.keys())
Rect = namedtuple('Rect', 'x y w h')
for claim_1, claim_2 in combinations(claims, 2):
    coord_1, size_1 = claims[claim_1]
    coord_2, size_2 = claims[claim_2]
    rect_1 = Rect(coord_1[0], coord_1[1], size_1[0], size_1[1])
    rect_2 = Rect(coord_2[0], coord_2[1], size_2[0], size_2[1])
    if (rect_1.x < rect_2.x + rect_2.w and rect_1.x + rect_1.w > rect_2.x and
        rect_1.y < rect_2.y + rect_2.h and rect_1.y + rect_1.h > rect_2.y):
        no_collision.discard(claim_1); no_collision.discard(claim_2)
print(no_collision)
