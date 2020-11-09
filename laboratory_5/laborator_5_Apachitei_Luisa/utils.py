def process_item(x):
    x+=1
    # while(any([x%el==0 for el in range(2,int(x**(1/2))+1)])):
    while (any([x % el == 0 for el in range(2, x//2 + 1)])):
        x+=1
    return x

def main():
    x = input("Enter number: ")
    try:
        x = int(x)
    except:
        print("Cannot convert to int")
    else:
        print(process_item(x))

if __name__=='__main__':
    main()