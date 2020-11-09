# Exercise 2
def functionSum(*args,**kwargs):
    return sum(kwargs.values())
function_Sum_Anonymous = lambda *args,**kwargs : sum(kwargs.values())

print(function_Sum_Anonymous(1,2,c=3,d=4))
print(functionSum(1,2,c=3,d=4))

# Exercise 3
def function3(string):
    return [ch for ch in string if ch.lower() in "aeiou"]
f3 = lambda string: [ch for ch in string if ch.lower() in "aeiou"]
f3_filter = lambda string: list(filter(lambda ch : ch.lower() in "aeiou",string))

print(function3("Programming in Python is fun"))
print(f3("Programming in Python is fun"))
print(f3_filter("Programming in Python is fun"))

# Exercise 4
def function_4(*args,**kwargs):
    """One line solution"""
    #return [item for item in list(args) + list(kwargs.values()) if type(item) == dict and len(item.keys()) >= 2 and any([type(key) == str and len(key) >= 3 for key in item.keys()])]
    """"""
    result = []
    values = list(args) + list(kwargs.values())
    for arg in values:
        if type(arg) == dict:
            if (len(arg.keys()) >= 2 and any([type(key) == str and len(key) >= 3 for key in arg.keys()])):
                result += [arg]
    return result

print(function_4(
{1: 2, 3: 4, 5: 6},

 {'a': 5, 'b': 7, 'c': 'e'},

 {2: 3},

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}
))

# Exercise 5

def function_5(lista):
    return [el for el in lista if type(el)==int or type(el)==float]

print(function_5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# Exercise 6

def function6(integers):
    return list(zip([el for el in integers if el%2==0],[el for el in integers if el%2!=0]))
print(function6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

# Exercise 7

def process(**kwargs):
    def Fibo(n):
        a = 0
        b = 1
        if n <= 0:
            print("Incorrect input")
            x = []
        elif n == 1:
            x = [b]
        else:
            x = [a, b]
            for i in range(2, n):
                c = a + b
                x += [c]
                a = b
                b = c
        return x
    fibo = Fibo(1000)
    if ("filters" in kwargs.keys()):
        fibo = [f for f in fibo if all([p(f) for p in kwargs["filters"]])]
    if ("offset" in kwargs.keys()):
        fibo = fibo[kwargs["offset"]:]
    if ("limit" in kwargs.keys()):
        return fibo[:kwargs["limit"]]
    return fibo


def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
))

# Exercise 8

#a
def multiply_by_two(x):
    return x * 2
def add_numbers(a, b):
    return a + b
def print_arguments(function):
    def f(*args,**kwargs):
        print(args,kwargs)
        return function(*args, **kwargs)
    return f

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)

#b
def multiply_output(function):
    def f(*args,**kwargs):
        return 2*function(*args,**kwargs)
    return f
def multiply_by_three(x):
    return x * 3
augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)

#c
def augment_function(function,decorators):
    def f(*args,**kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)
    return f
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x=decorated_function(3,4)
print(x)

# Exercise 9

def f9(pairs):
    return [{"sum":sum(el),"prod":el[0]*el[1],"pow":el[0]^el[1]} for el in pairs]
print(f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )) # will return [{'sum': 7, 'prod': 10, 'pow': 25}, {'sum': 20, 'prod': 19, 'pow': 19}, {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}] )



