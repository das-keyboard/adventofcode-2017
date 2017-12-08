stack = []


def process(uri: str):
    f = open(uri, 'r')
    maxi = 0
    for line in f:
        process_statement(line.replace('\n', '').strip())
        maxi = getmax() if getmax() > maxi else maxi
    print('All Time Max: ' + str(maxi))
    return getmax()


def process_statement(statement: str):
    global stack
    par = statement.split(' ')  # Alway len = 7
    case = par[5]
    var = par[4]
    val = int(par[6])
    if case == '>' and getvar(var) <= val:
        return
    elif case == '<' and getvar(var) >= val:
        return
    elif case == '>=' and getvar(var) < val:
        return
    elif case == '<=' and getvar(var) > val:
        return
    elif case == '==' and getvar(var) != val:
        return
    elif case == '!=' and getvar(var) == val:
        return

    if par[1] == 'inc':
        setvar(par[0], getvar(par[0]) + int(par[2]))
    elif par[1] == 'dec':
        setvar(par[0], getvar(par[0]) - int(par[2]))
    return


def getvar(var: str):
    global stack
    for i in stack:
        if i[0] == var:
            return int(i[1])
    stack.append([var, 0])
    return 0


def setvar(var: str, val: int):
    global stack
    for i in stack:
        if i[0] == var:
            i[1] = val
            return
    stack.append([var, val])
    return


def getmax():
    global stack
    mini = stack[0][1]
    for i in stack:
        mini = i[1] if i[1] > mini else mini
    return int(mini)


print(process('input_t'))
print(process('input'))
