import math


def fibo_n(n):
    if n == 0 or n == 1:
        return n
    fibo_0 = 0
    fibo_1 = 1

    for i in range(1, n):
        aux = fibo_1 + fibo_0
        fibo_0 = fibo_1
        fibo_1 = aux

    return fibo_1

# 1
def fibo_list(n):
    return [fibo_n(i) for i in range(1, n)]
print(fibo_list(30))


# 2

def prime_test(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def primes_in_list(x):
    return [i for i in x if prime_test(i) == True]

print(primes_in_list(range(1, 400)))

# 3
a = [2, 3, 4, 5, 6]
b = [1, 2, 3, 4]


def a_and_b(a, b):
    return [i for i in a if i in b]


def a_minus_b(a, b):
    return [i for i in a if i not in b]


def a_u_b(a, b):
    list_a = a[:]
    list_a.extend([i for i in a_minus_b(b, a)])
    return list_a


print(a_u_b(a, b), a_and_b(a, b), a_minus_b(a, b), a_minus_b(b, a))


#5

given_matrix= [[1,1,1],
                [1,1,1],
                [1,1,1]]


def matrix_manipulation(matrix):

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):

            if i == j:
                break

            matrix[i][j] = 0


matrix_manipulation(given_matrix)

print(given_matrix)


# 8

def char_filter(strings, number=1, flag=True):
    ret_list = []

    for index, char_set in enumerate(strings):
        ret_list.append([])
        # List comprehensionul de mai jos este folosit doar pt efectul secundar al apelarii metodei append. Lista
        # rezultata este "aruncata la gunoi".
        [ret_list[index].append(j) for j in char_set if (ord(j) % number == 0) == flag and j not in ret_list[index] ]

    return ret_list


def char_filter_2(strings, number=2, flag=True):
    return [[i] for j in strings for i in j if ord(i) % number == 1 - int(flag)]


print(char_filter(['abcde', 'dsadadsa', 'dasdsadsa'], 2))
print(char_filter_2(['abcde', 'dsadadsa', 'dasdsadsa'])) # am incercat si o varianta one line; nu intoarce chiar ce vreau


# 11
test = [('abc', 'bcd'), ('abc', 'zza')]


def sort_list(given_list):
    return given_list.sort(reverse = False, key=lambda element: element[1][2])


print(sort_list(test))














