result = 0
seen = set()
while True:
    for line in open('input.txt'):
        result += eval(line)
        if result in seen: print(result)
        else: seen.add(result)