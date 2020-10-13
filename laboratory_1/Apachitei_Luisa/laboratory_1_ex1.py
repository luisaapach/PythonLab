print("How many numbers?")
how_many = int(input())

n1 = int(input("Give me %(numbers)d numbers\n" % {"numbers": how_many}))
cmmdc = n1
for i in range(1, how_many):
    n2 = int(input())
    while (n2 != cmmdc):
        if n2 > cmmdc:
            n2 = n2 - cmmdc
        else:
            cmmdc = cmmdc - n2
print(cmmdc)