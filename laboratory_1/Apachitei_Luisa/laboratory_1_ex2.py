"""solutia 1 - parcurgere vowels"""
vowels = "aeiou"
string = input()
string = string.lower()
count = 0
for v in vowels:
    c_v = string.count(v)
    if(c_v != -1):
        count += c_v
print(count)
"""solutia 2 - parcurgere string"""
count = 0
for ch in string:
    if ch in vowels:
        count+=1
print(count)

"""solutia 3 - suma de count-uri de vocale"""
print(sum([0 if v not in string else string.count(v) for v in vowels]))
"""solutia 4 - filtrare pe list"""
print(len([ch for ch in string if ch in vowels]))
