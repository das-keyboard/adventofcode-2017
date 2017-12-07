
def process(uri: str):
    f = open(uri, 'r')
    programms = []
    childs = ''
    for line in f:
        programms.append(line.split(' ')[0])
        if '->' in line:
            childs += ' ' + line.split('->')[1]

    for programm in programms:
        if programm not in childs:
            print(programm)


print(process('input'))
