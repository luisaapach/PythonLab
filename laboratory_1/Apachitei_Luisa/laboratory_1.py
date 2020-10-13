def function5():
    print("Give the size of square")
    square_n = int(input())
    s = []
    for i in range(0,square_n):
        s+=[input()]

    r = 0
    c = 0
    r_n = square_n
    c_n = square_n
    final_result = ""
    while (r < r_n and c < c_n):
        for i in range(r, c_n):
            final_result += s[c][i]
        c += 1
        for i in range(c, r_n):
            final_result += s[i][c_n - 1]
        c_n -= 1
        if (c < r_n):
            for i in range(c_n-1, r-1, -1):
                final_result += s[r_n-1][i]
            r_n -= 1
        if(r < c_n):
            for i in range(r_n-1, c-1, -1):
                final_result += s[i][r]
            r += 1
    return final_result

def function6(number):
    """solutia one-line
    puteati face si varianta in care sa parcurgeti literele si sa apendati in fata la un alt string"""
    return str(number) == str(number)[::-1]

def function7(text):
    """solutia 1
    parcurg pana gasesc o cifra
    daca o gasesc, parcurg pana cand mai gasesc cifre
    returnez intervalul in care am gasit numarul
    """
    c = 0
    while(c<len(text) and not text[c].isdigit()):
        c+=1
    if(c==len(text)):
        print("No numbers")
        return
    d = c
    while(d<len(text) and text[d].isdigit()):
        d+=1
    if(d==len(text)):
        d=-1
    return text[c:d]
    """solutia 2"""
    for i in range(len(text)):
        if text[i].isdigit():
            s_idx = i
            while i < len(text) and text[i].isdigit():
                i += 1
            return text[s_idx:i]
    print("No numbers")

def dec_to_bin(number):
    if(number == 0):
        return ""
    else:
        return dec_to_bin(number//2) + str(number%2)

def function8(number):
    """solutia 1"""
    bin_number = ""
    while(number!=0):
        bin_number = str(number%2) + bin_number
        number = number//2
    return bin_number.count("1")
    """solutia 2
    identic cu 1 dar recursiva"""
    return dec_to_bin(number).count("1")
    """solutia 3
    folosim functia bin(nr)"""
    return bin(number).count("1")
    """solutia 4"""
    count=0
    while(number!=0):
        number&=(number-1)
        count+=1
    return count
    """solutia 5"""
    count = 0
    while (number != 0):
        count += number%2
        number>>=1
    return count


def function9(text):
    """solutia 1
    - one line"""
    text=text.lower()
    return max([(el, text.count(el)) for el in text if el.isalpha()] if text != "" else [("", 0)],
               key=lambda t: t[1])
    """solutia 2
    - count de fiecare data si comparat cu maximul
    - pt eficientizare, retineti numerele care au fost parcurse ca sa nu le mai renumarati"""
    #parcurse = "" #optional daca nu vreti sa faceti count de 2 ori acelasi ch
    maxi = 0
    letter = ""
    text = text.lower()
    for el in text:
        if(el.isalpha()):
            count = text.count(el)
            if(count > maxi) :
                maxi = count
                letter=el
    return letter

def function10(text):
    """solutia 1 one line"""
    return len(text.split(" "))-text.split(" ").count("")
    """solutia 2 - in cazul in care existau mai multe spatii"""
    nr = 0
    words = text.split(" ")
    for i in range(len(words)):
        if len(words[i])!=0:
            nr += 1
    return nr

