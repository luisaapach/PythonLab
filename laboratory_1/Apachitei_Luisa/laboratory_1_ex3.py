import sys
if (len(sys.argv) == 3):
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(s2.count(s1))
    # rezolvare corecta daca vrem ca pt s2 (ex. = "ananana") sa dea 3 !
    count = 0
    for i in range(len(s2)):
        if(s2[i:].startswith(s1)):
            count+=1
    print(count)
else:
    print("Not valid arguments")