from collections import defaultdict, namedtuple

claims = {}
for line in open('input.txt'):
    spl_line = line.split()
    value_list = [spl_line[2][:-1].split(','), spl_line[3].split('x')]
    value_list[0] = list(map(int, value_list[0]))
    value_list[1] = list(map(int, value_list[1]))
    claims[spl_line[0][1:]] = value_list

coords = defaultdict(int)
Rect = namedtuple('Rect', 'x y w h')
for claim in claims:
    coord, size = claims[claim]
    rect = Rect(coord[0], coord[1], size[0], size[1])
    for i in range(rect.w):
        for j in range(rect.h):
            coords[(rect.x + i, rect.y + j)] += 1
print(sum(1 for i in coords.values() if i > 1))
