def fibonacciN(n):
    fibo = [1, 1]
    if n == 2:
        return fibo
    for i in range(2, n):
        fibo += [fibo[i - 2] + fibo[i - 1]]
    return fibo

def exercise2(numbers):
    primes = [x for x in numbers if len([y for y in range(2, x//2 + 1) if x % y == 0]) == 0]
    return primes

def exercise3(a, b):
    intersection = [x for x in a if x in b]
    union = a + [y for y in b if y not in a]
    aMinusB = [x for x in a if x not in b]
    bMinusA = [y for y in b if y not in a]
    return intersection, union, aMinusB, bMinusA


def exercise4(notes, moves, start):
    song = list()
    note = start
    song += [notes[note]]
    for step in moves:
        note = (note + step) % len(notes)
        song += [notes[note]]

    return song


def exercise5(matrix):
    for line in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            if line > column:
                matrix[line][column] = 0

    return matrix


def exercise6(*args):
    x = int(args[-1][0])
    myList = list()
    for lists in args:
        myList += lists
    del myList[-1]
    myList = [x for x in myList if isinstance(x, int)]

    numbers = list()

    i = 0
    myList.sort()
    while i < len(myList):
        if myList.count(myList[i]) == x:
            numbers += [myList[i]]
        i += myList.count(myList[i])

    return numbers


def exercise7(a):
    count = len([x for x in a if x == int(str(x)[::-1])])
    maxi = max([x for x in a if x == int(str(x)[::-1])])
    t = (count, maxi)
    return t


def exercise8(x, a, flag):
    asciiList = list()
    for i in a:
        word = list()
        for j in i:
            if (ord(j) % x == 0) == flag:
                word += j
        asciiList += [word]

    return asciiList


def exercise9(matrix):
    maxis = matrix[0]
    i = 1
    j = 0
    unluckys = list()
    while i < len(matrix):
        j = 0
        while j < len(maxis):
            if matrix[i][j] <= maxis[j]:
                unluckys += [(i, j)]
            else:
                maxis[j] = matrix[i][j]
            j += 1
        i += 1

    return unluckys

def exercise10(*args):
    result = list()
    myList = list()
    lgMax = 0
    i = 0
    j = 0
    for l in args:
        if len(l) > lgMax:
            lgMax = len(l)
        myList += [l]

    for j in range(0, lgMax):
        i = 0
        t = list()
        while i < len(myList):
            if j >= len(myList[i]):
                t += [None]
            else:
                t += (myList[i][j])
            i += 1
        result += [(t)]

    return result


def exercise11(a):
    a.sort(key = lambda i: i[1][2])

    return a

