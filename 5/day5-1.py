def process(uri: str):
    f = open(uri, 'r')
    index = 0
    arr = [int(x) for x in f]
    steps = 0
    while 0 <= index < len(arr):
        steps += 1
        step = arr[index]
        arr[index] += 1
        index += step
        # print(index)
    return steps


print(process('input_t'))
print(process('input'))
