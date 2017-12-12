import sys

sum = 0

def process(uri: str):
    global sum
    sum = 0

    line = open(uri, 'r').readline().replace('\n', '').strip()
    data = []
    for char in line:
        data.append(char)

    # Remove '!' and the following
    while '!' in data:
        for i in data:
            if i == '!':
                index = data.index(i)
                del data[index]
                del data[index]

    # remove Garbage
    while '<' in data:
        opened = False
        index = 0
        for i in data:
            if i == '<' and not opened:
                opened = True
                index = data.index(i)
            if i == '>' and opened:
                del data[index:(data.index(i) + 1)]
                opened = False
    print(listtostr(data))
    getgroups(listtostr(data), 1)
    print(str(sum))


def getgroups(text: str, off: int):
    global sum
    if text == '':
        return
    if isvalidgroup(text):
        groups = text.split(',')
        for group in groups:
            sum += off
            # print(group)
            arr = [x for x in group]
            del arr[arr.index('{')]
            del arr[len(arr) - 1 - arr[::-1].index('}')]
            getgroups(listtostr(arr), off + 1)
    else:
        sum += off
        # print(text)
        arr = [x for x in text]
        del arr[arr.index('{')]
        del arr[len(arr) - 1 - arr[::-1].index('}')]
        getgroups(listtostr(arr), off + 1)


def isvalidgroup(lst: str):
    valid = True
    groups = lst.split(',')
    for group in groups:
        if '{' in group and '}' in group:
            if group.count('{') != group.count('}'):
                valid = False
    return valid


def listtostr(lst):
    st = ''
    for i in lst:
        st += i
    return str(st)


sys.setrecursionlimit(9999)
process('input')


