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
        for i in entry:
            for j in entry:
                if (i != j) & (sorted(i) == sorted(j)):
                    isvalid = False
        if isvalid:
            sum += 1
    return sum


# print(process('input_t'))
print(process('input'))
