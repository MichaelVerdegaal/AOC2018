polymer = open('input.txt').readline()[:-1]

def combust(poly_list: list) -> int:
    size = len(poly_list)
    index = 0
    while index < size - 1:
        if index < 0:
            index = 0
        unit1, unit2 = poly_list[index], poly_list[index + 1]
        if unit1 != unit2 and unit1.lower() == unit2.lower():
            del poly_list[index]
            del poly_list[index]
            size -= 2
            index -= 2
        index += 1
    return size

possible_poly = set()
for unit in polymer:
    if not unit == unit.lower():
        continue
    if unit not in possible_poly:
        possible_poly.add(unit)
smallest = None
for excluded_unit in possible_poly:
    polmerList = list(polymer.replace(excluded_unit, '').replace(excluded_unit.upper(), ''))
    poly_size = combust(polmerList)
    if smallest is None or poly_size < smallest:
        smallest = poly_size

print(smallest)