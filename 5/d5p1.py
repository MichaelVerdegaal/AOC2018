polymer = list(open('input.txt').readline())[:-1]
size = len(polymer)
index = 0
while index < size - 1:
    if index < 0:
        index = 0
    unit1, unit2 = polymer[index], polymer[index + 1]
    if unit1 != unit2 and unit1.lower() == unit2.lower():
        del polymer[index]; del polymer[index]
        size -= 2; index -= 2
    index += 1
print(size)
