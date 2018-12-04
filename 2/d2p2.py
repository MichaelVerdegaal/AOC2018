from itertools import combinations
for box_id, box_id_2 in combinations(open('input.txt'), 2):
    letter_diff = 0
    for char1, char2 in zip(box_id, box_id_2):
        if char1 != char2: letter_diff += 1
        if letter_diff > 1: break
    else:
        print("".join(char1 for char1, char2 in zip(box_id, box_id_2) if char1 == char2))