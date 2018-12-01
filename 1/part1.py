result = 0
for line in open('input.txt'):
    result += eval(line)
print(result)