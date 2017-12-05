def process(uri: str):
    f = open(uri, 'r')
    index = 0
    arr = [int(x) for x in f]
    steps = 0
    while 0 <= index < len(arr):
        steps += 1
        step = arr[index]
        if step >= 3:
            arr[index] -= 1
        else:
            arr[index] += 1
        index += step
    return steps


print(process('input_t'))
print(process('input'))
