# ex1
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def exercise1():
    """
    Write a function to return a list of the first n numbers in the Fibonacci string.
    """
    n = int(input("Enter a positive number: \n"))
    return [fibonacci(nr) for nr in range(1, n + 1)]

print(exercise2())


# ex3
def exercise3(a, b):
    """
    Write a function that receives as parameters two lists a and b and returns:
    (a intersected with b, a reunited with b, a - b, b - a)
    """
    a_intersected_b = [n for n in a if n in b]
    a_b = [n for n in a if n not in b]
    b_a = [n for n in b if n not in a]
    a_reunited_b = a_b + b_a
    return sorted(a_intersected_b), sorted(a_reunited_b), sorted(a_b), sorted(b_a)

print(exercise3([1, 3, 45, 20, 4], [45, 2, 1, 23, 36]))


# ex5
def exercise5(m):
    """
    Write a function that receives as parameter a matrix and will return
    the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
    """
    print(m)
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if i > j:
                m[i][j] = 0
    print(m)

print(exercise5([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))