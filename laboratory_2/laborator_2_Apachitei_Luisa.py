"""
   1. Write a function to return a list of the first n numbers in the Fibonacci string.
"""
def function1(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
        x=[]
    elif n == 1:
        x=[b]
    else:
        x=[a,b]
        for i in range(2,n):
            c = a + b
            x+=[c]
            a = b
            b = c
    return x


def function1_recursive(n):
    if(n<=0):
        return []
    elif(n==1):
        return [0]
    elif(n==2):
        return [0,1]
    else:
        s1 = function1_recursive(n-2)
        s2 = function1_recursive(n-1)
        return  s1+[s2[-1],s1[-1]+s2[-1]]

"""
2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
"""
def function2(list):
    return [x for x in list if len([y for y in range(2,x//2+1) if x%y==0])==0]

"""
3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
"""
def intersection(list1,list2):
    list3 = []
    for el in list1:
        if el in list2 and el not in list3:
            list3+=[el]
    return list3
    # return list(set(list1)&set(list2))
def reunion(list1,list2):
    list3 = []
    for el in list1:
        if el not in list3:
            list3 += [el]
    for el in list2:
        if el not in list3:
            list3 += [el]
    return list3
    #return list(set(list1) | set(list2))
def diference(list1,list2):
    list3 = []
    for el in list1:
        if el not in list2 and el not in list3:
            list3 += [el]
    # list3.sort()
    return list3
    # return list(set(list1)-set(list2))
def function3(list1, list2):
    print(list1)
    print(list2)
    print("")
    print(intersection(list1,list2))
    print(reunion(list1,list2))
    print(diference(list1,list2))
    print(diference(list2, list1))
    return (intersection(list1,list2), reunion(list2,list1), diference(list1,list2), diference(list2,list1))

"""
4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 
"""
def compose(notes, moves, start):
    new_notes = [notes[start]]
    last_index = start
    for move in moves:
        new_index = (last_index + move) % len(notes)
        new_notes+=[notes[new_index]]
        last_index = new_index
    return new_notes

"""
 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
"""
def function5(matrix):
    lines = len(matrix)
    if not all(list(map(lambda i : i == lines, [len(i) for i in matrix]))):
        print("Invalid matrix")
        return
    if len(list(filter(lambda i : i == lines, [len(i) for i in matrix]))) != lines:
        print("Invalid matrix")
        return
    # j<i
    for i in range(lines):
        for j in range(i):
            matrix[i][j] = 0
    return matrix

"""
 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. 
"""
def function6(x,*list_of_lists):
    if (len(list_of_lists) == 0):
        return []
    # concat = []
    # final_list = []
    # for el in list_of_lists:
    #     concat += el
    # for el in concat:
    #     if (concat.count(el) == x and el not in final_list):
    #         final_list += [el]
    # return final_list
    #sau
    freq = []
    unique = []
    for l in list_of_lists:
        for el in l:
            if(el not in unique):
                unique+=[el]
                freq+=[1]
            else:
                freq[unique.index(el)]+=1
    #return [el for i,el in enumerate(unique) if freq[i]==x]
    #sau
    return [el for el,fr in zip(unique,freq) if fr==x]

"""
  7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
"""
def function7(list_of_integers):
    palindroms = [el for el in list_of_integers if str(el) == str(el)[::-1]]
    return (len(palindroms),max(palindroms))

"""
 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.
"""
def function8(list_of_strings, x = 1, flag = True):
    final_list = []
    for sir in list_of_strings:
        if flag:
            final_list += [[el for el in sir if ord(el) % x == 0]]
        else:
            final_list += [[el for el in sir if ord(el) % x != 0]]
    return final_list

"""
 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
"""
def function9(matrix):
    not_ok = []
    for i in range(1,len(matrix)):
        for j in range(0,len(matrix[0])):
            #print("elem {},{}".format(i,j))
            if not all(list(map(lambda el: matrix[el][j]<matrix[i][j],range(0,i)))):
                not_ok+=[(i,j)]
            # g_s = True
            # for el in range(0,i):
            #     g_s &= (matrix[el][j]<matrix[i][j])
            # if not g_s:
            #     not_ok+=[(i,j)]
    return not_ok
    #sau
    list_of_positions = []
    matrix_transpose = list(zip(*matrix))
    for c in range(len(matrix_transpose)):
        for l in range(1, len(matrix_transpose[0])):
            if matrix_transpose[c][l] <= max(matrix_transpose[c][:l]):
                list_of_positions.append(tuple((l, c)))
    return list_of_positions

"""
10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists,..
"""
def function10(*lists):
    max_no_of_elements = max([len(x) for x in lists])
    new_lists = [l + [None for i in range(len(l) + 1, max_no_of_elements + 1)] for l in lists]
    return list(zip(*new_lists))

"""
11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
"""
def function11(*lists):
    if (len([l for l in lists if len(l) < 2]) != 0):
        print("Incorrect input")
        return []
    # lists.sort(key=lambda el : el[1][2])
    # return lists
    return sorted(lists, key=lambda el: el[1][2])

"""
 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
"""
def group_by_rhyme(list_of_words):
    # last_letters = []
    # for el in list_of_words:
    #     if el[-2:] not in last_letters:
    #         last_letters+=[el[-2:]]
    # final_list = []
    # for last in last_letters:
    #     final_list+=[[el for el in list_of_words if el[-2:] == last]]
    # return final_list
    list_of_words.sort(key=lambda el:el[-2:])
    final_list = []
    for el in list_of_words:
        if len(final_list)>0 and (el[-2:]==final_list[-1][-1][-2:]):
            final_list[-1]+=[el]
        else:
            final_list+=[[el]]
    return final_list
