def process(uri: str):
    f = open(uri, 'r')
    stack = [int(x) for x in f.readline().replace('\n', '').strip().split('\t')]
    prev_sets = []
    steps = 0
    while str(stack) not in prev_sets:
        prev_sets.append(str(stack))
        maxb = max(stack)
        index = stack.index(maxb)
        stack[index] = 0
        for i in range(maxb):
            index = (index + 1) if index != len(stack) - 1 else 0
            stack[index] += 1
        steps += 1
    return steps


print(process('input_t'))
print(process('input'))


