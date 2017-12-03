
def getsidelen(num: int):
    i = 3
    while True:
        if i*i > num:
            return i
        i += 2


# inp = 44
inp = 361527
steps = 0
field = getsidelen(inp)
print(field)   # we need 603x603 fields = 363609
steps += field // 2    # steps to the center of 1 of the axis
diff = 0
mid1 = (field * field) - field // 2
diff = abs(inp - mid1)
for i in range(3):  # which center is the nearest one?
    mid1 -= (field - 1)
    if abs(inp - mid1) < diff:
        diff = abs(inp - mid1)
steps += diff   # steps to center 2nd axis
print(steps)

