# exercise 3
"""
Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate
 a list with all the vowels in a given string.
For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
"""


def method1(string):
    return [c for c in string if c in "aeiouAEIOU"]


def method2(string):
    return list(filter(lambda c: c in "aeiouAEIOU", string))


def method3(string):
    vowels = []
    for c in string:
        if c in "aeiouAEIOU":
            vowels.append(c)
    return vowels


# exercise 4
def exercise4(*arguments):
    """
Write a function that receives a variable number of arguments and keyword arguments.
The function returns a list containing only the arguments which are dictionaries,
 containing minimum 2 keys and at least one string key with minimum 3 characters.
Example: my_function( {1: 2, 3: 4, 5: 6},
                      {'a': 5, 'b': 7, 'c': 'e'},
                      {2: 3},
                      [1, 2, 3],
                      {'abc': 4, 'def': 5},
                      3764,
                      dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                      test={1: 1, 'test': True} )
will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]
    """
    dic = []
    for a in arguments:
        if type(a) is dict:
            if len(str(a)) >= 2:
                for k in a.keys():
                    if len(str(k)) >= 3:
                        dic.append(a)
                        break
    return dic


# exercise 5
def exercise5(lista):
    """
    Write a function with one parameter which represents a list. The function will return a new list
     containing all the numbers found in the given list.
    Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]
    """
    return [i for i in lista if type(i) == int or type(i) == float]


# exercise 6
def exercise6(integers):
    """
    Write a function that receives a list with integers as parameter that contains an equal number of even
     and odd numbers that are in no specific order. The function should return a list of pairs
     (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list
     and Yi is the i-th odd number.
    Example: my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]
    """
    x = [i for i in integers if i % 2 == 0]
    y = [i for i in integers if i % 2 != 0]
    return [(x, y) for x, y in zip(x, y)]


# exercise 7
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# exercise 9
def exercise9(pairs):
    """
    Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs).
     The function should return a list of dictionaries for each pair (in the same order as in the input list)
     that contain the following keys (as strings): sum (the value should be sum of the 2 numbers),
     prod (the value should be product of the two numbers),
     pow (the value should be the first number raised to the power of the second number).
    Example: f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )
     will return [{'sum': 7, 'prod': 10, 'pow': 25}, {'sum': 20, 'prod': 19, 'pow': 19},
                  {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}]
    """
    dict_list = []
    for p in pairs:
        x, y = p
        dict_list.append({'sum': sum(p),
                          'prod': x*y,
                          'pow': pow(x, y)})
    return dict_list
