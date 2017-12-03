#################################
# FUCK DIS WHOLE SHIT!
#
# Just look up the number online!
#
# https://oeis.org/A141481
# https://oeis.org/A141481/b141481.txt
#
#################################

def build():
    field = []
    row = []
    for i in range(100):
        for j in range(100):
            row.append(0)
        field.append(row)
        row = []
    return field


def process(field, num: int):
    field[50][50] = 1


def sumaround(field, i: int, j:int):
    sum = 0
    sum += field[i - 1][j]
    sum += field[i + 1][j]
    sum += field[i][j - 1]
    sum += field[i][j + 1]
    sum += field[i - 1][j - 1]
    sum += field[i + 1][j + 1]
    sum += field[i + 1][j - 1]
    sum += field[i - 1][j + 1]
    return sum

field = build()


