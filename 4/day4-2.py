import itertools


def process(uri: str):
    file = open(uri, 'r')
    valid = []
    sum = 0
    for line in file:
        ln = line.strip().replace('\n', '').split(' ')
        if len(ln) == len(set(ln)):
            valid.append(ln)
    for entry in valid:
        isvalid = True
        for x, y in itertools.combinations(entry, 2):
            if sorted(x) == sorted(y):
                isvalid = False
        if isvalid:
            sum += 1
    return sum


# print(process('input_t'))
print(process('input'))
