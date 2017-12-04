def process(uri: str):
    file = open(uri, 'r')
    sum = 0
    for line in file:
        ln = line.strip().replace('\n', '').split(' ')
        if len(ln) == len(set(ln)):
            sum += 1
    return sum


# print(process('input_t'))
print(process('input'))
