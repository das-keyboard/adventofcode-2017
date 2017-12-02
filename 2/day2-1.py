def process(uri: str):
    sum = 0
    file = open(uri, 'r')
    for line in file:
        sum += getdiff(line.replace('\t', ' ').replace('\n', '').split(' '))
    return sum


def getdiff(nums):
    nums = [int(x) for x in nums]
    min = nums[0]
    max = nums[0]
    # Using sort() would be boring...
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    return int(max - min)


print(process('sheet_t1'))   # 18
print("Let's get real!")
print(process('sheet_1'))
