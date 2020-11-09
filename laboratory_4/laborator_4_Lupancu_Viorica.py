import os
import sys


# ex1
def exercise1(director):
    """
    S? se scrie o func?ie ce primeste un singur parametru, director, ce reprezint? calea c?tre un director.
    Func?ia returneaz? o list? cu extensiile unice sortate crescator(in ordine alfabetica) a fi?ierelor
     din directorul dat ca parametru.
    Men?iune: extensia fi?ierului ‘fisier.txt’ este ‘txt’.
    """
    extension_list = []
    print(os.listdir(director))
    for file in os.listdir(director):
        if len(os.path.splitext(file)[1]) > 0:
            extension_list.append(os.path.splitext(file)[1][1:])
    extension_list = set(extension_list)
    return sorted(extension_list)


# ex2
def exercise2(director, file):
    """
    S? se scrie o func?ie ce prime?te ca argumente dou? c?i: director si fi?ier.
    Implementati functia astfel încât în fi?ierul de la calea fi?ier s? fie scris? pe câte o linie,
     calea absolut? a fiec?rui fi?ier din interiorul directorului de la calea folder, ce incepe cu litera A.
    """
    try:
        f = open(file, "w")
        for d in os.listdir(director):
            if len(os.path.splitext(d)[1]) > 0 and \
                    (os.path.splitext(d)[0][0] == "D" or os.path.splitext(d)[0][0] == "d"):
                f.write(os.path.abspath(d) + "\n")
        f.close()
    except Exception as e:
        print(str(e))


# ex4
def exercise4():
    """
    S? se scrie o func?ie ce returneaz? o list? cu extensiile unice a fi?ierelor din directorul dat ca argument
     la linia de comand? (nerecursiv). Lista trebuie s? fie sortat? cresc?tor.
    Men?iune: extensia fi?ierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie,
     deci nu va ap?rea în lista final?.
    """
    extension_list = []
    director = sys.argv[1]
    print(os.listdir(director))
    for file in os.listdir(director):
        if len(os.path.splitext(file)[1]) > 0:
            extension_list.append(os.path.splitext(file)[1][1:])
    extension_list = set(extension_list)
    return sorted(extension_list)


# ex7
def exercise7(file):
    """
    S? se scrie o func?ie care prime?te ca parametru un ?ir de caractere care reprezint? calea c?tre un fi?er
     si returneaz? un dic?ionar cu urm?toarele c?mpuri: full_path = calea absoluta catre fisier,
     file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
     can_read, can_write = True/False daca se poate citi din/scrie in fisier.
    """
    if os.path.isfile(file):
        dic = {"full_path": os.path.abspath(file),
               "file_size": os.stat(file).st_size,
               "file_extension": os.path.splitext(file)[1][1:],
               "can_read": os.access(file, os.R_OK),
               "can_write": os.access(file, os.W_OK)}
    else:
        dic = {}
    return dic


# ex8
def exercise8(dir_path):
    """
    S? se scrie o func?ie ce prime?te un parametru cu numele dir_path. Acest parametru reprezint? calea c?tre
     un director aflat pe disc. Func?ia va returna o list? cu toate c?ile absolute ale fi?ierelor aflate în
     r?d?cina directorului dir_path.
    Exemplu apel func?ie: functie("C:\\director") va returna
     ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
    """
    file_list = []
    for (root, directories, files) in os.walk(dir_path):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))
    return file_list
