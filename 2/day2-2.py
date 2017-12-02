def process(uri: str):
    sum = 0
    file = open(uri, 'r')
    for line in file:
        sum += getsum(line.replace('\t', ' ').replace('\n', '').split(' '))
    return sum


def getsum(nums):
    nums = [int(x) for x in nums]
    sum = 0
    for num in nums:
        for num2 in nums:
            if (num != num2) & (int(num) % int(num2) == 0):
                sum += num / num2
    return sum


print(process('sheet_t2'))   # 9
print("Let's get real!")
print(process('sheet_1'))
