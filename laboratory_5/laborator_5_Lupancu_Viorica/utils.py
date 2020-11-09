__doc__ = """
1) 
a) Write a module named utils.py that contains one function called process_item. 
The function will have one parameter, x, and will return the least prime number greater than x.
When run, the module will request an input from the user, convert it to a number and it will display 
 the output of the process_item function.
"""


def process_item(x):
    max_size = int(1e6)
    for i in range(x + 1, max_size):
        nr = 0
        for j in range(1, i + 1):
            if (i % j) == 0:
                nr += 1
        if nr == 2:
            return i


if __name__ == "__main__":
    try:
        print(process_item(int(input("Enter an integer: \n"))))
    except Exception as e:
        print(e)
