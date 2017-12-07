# DO NOT LOOK AT THIS CODE
#
# Just go along..
#
# Lokk at something pretty instead...
############################################


def process(uri: str):
    f = open(uri, 'r')
    programms = []

    # Save all programms (with their children) into an array
    for line in f:
        prog = []
        prog.append(line.split(' ')[0])
        prog.append(line.split(' ')[1].replace('(', '').replace(')', ''))
        if '->' in line:
            prog.append(line.split('->')[1].replace(',', '').replace('\n', '').strip().split(' '))
        else:
            prog.append([])
        programms.append(prog)

    # Save the weight of every programm into an array
    # Don't do this for the main root (from part 1)
    anotherarr= []
    for programm in programms:
        if programm[0] != 'svugo':
            anotherarr.append(getprogrammweight(programms, programm[0]))

    # If a value is there only once - this comes from an unbalanced path
    signle = []
    for i in anotherarr:
        if anotherarr.count(i) == 1:
            signle.append(i)

    # The lowest value should be the root of the unbalance
    # Search for this programm. It weight has to be changed
    search = []
    for programm in programms:
        if getprogrammweight(programms, programm[0]) == min(signle):
            search = programm
            print('Programm: ' + str(search) + '\nChilds:')
            for i in search[2]:
                print(i + ': ' + str(getprogrammweight(programms, i)))

    # Search the parent programm of the previous found one.
    # This shows how much the value differs from the other values
    for programm in programms:
        if search[0] in programm[2]:
            print('\nProgramm: ' + str(programm) + '\nChilds:')
            for i in programm[2]:
                print(i + ': ' + str(getprogrammweight(programms, i)))


def getprogrammweight(programms, pro: str):
    sum = 0
    for programm in programms:
        if programm[0] == pro:
            if len(programm[2]) > 0:
                for prog in programm[2]:
                    a = getprogrammweight(programms, prog)
                    sum += a
                return int(sum + int(programm[1]))
            else:
                return int(programm[1])
    return 0


process('input')
