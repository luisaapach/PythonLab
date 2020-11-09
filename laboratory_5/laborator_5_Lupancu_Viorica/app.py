__doc__ = """
1)
b) Write a module named app.py. When this module is run, it will run in an infinite loop, 
waiting for inputs from the user. 
The program will convert the input to a number and process it using the function process_item implented in utils.py.
You will have to import this function in your module. The program stops when the user enters the message "q".
"""

from utils import process_item

if __name__ == "__main__":
    print("Enter some integers. Press q to stop!")
    x = input()
    while x != "q":
        try:
            x = int(x)
            print(process_item(x))
        except Exception as e:
            print(e)
        x = input()
