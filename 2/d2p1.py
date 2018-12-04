letter2, letter3 = 0, 0
for box_id in open('input.txt'):
    counter = dict()
    for char in box_id:
        counter[char] = counter.get(char, 0) + 1
    if 2 in counter.values(): letter2 += 1
    if 3 in counter.values(): letter3 += 1
print(letter2 * letter3)