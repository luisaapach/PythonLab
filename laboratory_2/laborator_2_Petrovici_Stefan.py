import re
"""
Ex 1
"""
def fib_n(n):
    arr = [0, 1]
    for i in range(n):
        arr.append(arr[-1] + arr[-2])
    return arr

"""
Ex 3
"""

def set_intersect(a: set, b: set):
    return set([x for x in a if x in b])


def set_add(a: set, b: set):
    return set([x for x in a] + [x for x in b])


def set_minus(a: set, b: set):
    return set([x for x in a if x not in b])


"""
Ex 4
"""

def compose(notes, nums, start):
    return [notes[(start + sum(nums[:i])) % len(notes)] for i, x in enumerate([0] + nums)]


"""
Ex 5
"""

def replace_main_diag(m):
    return [[(x if j <= i else 0) for i, x in enumerate(a)] for j, a in enumerate(m)]

"""
Ex 9
"""

def get_heights(m):
    # R: [[[(i, z) for z in range(len(m[0])) if m[i][z] < m[j][z]] for i in range(len(m)) if i > j] for j in range(len(m))]
    """return \
        [
            [
                [
                    (i, z)
                    for z in range(len(m[0]))
                        if m[i][z] < m[j][z]
                ]
                for i in range(len(m))
                    if i > j and len([(i, z) for z in range(len(m[0])) if m[i][z] < m[j][z]]) > 0
            ]
            for j in range(len(m))
                if len([[(i, z) for z in range(len(m[0])) if m[i][z] < m[j][z]] for i in range(len(m)) if i > j]) > 0
        ]
    """
    res = [[[(i, z) for z in range(len(m[0])) if m[i][z] <= m[j][z]] for i in range(len(m)) if i > j] for j in range(len(m))]
    return [eval(x) for x in set(re.findall("\([0-9], [0-9]\)", str(res)))]


"""
Ex 11
"""

def sortsort(lst: list):
    return sorted(lst, key=lambda x: x[1][2])

"""
Ex 12
"""

def rhyme(lst: list):
    #return [eval(x) for x in re.findall('\[[^\[]+\]', str([[b for b in lst if a[-2:] == b[-2:]] for a in lst]))]
    return [[b for b in lst if a[-2:] == b[-2:]] for a in lst]
