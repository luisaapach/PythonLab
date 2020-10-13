import sys

string = sys.argv[1]
idx = 0
final_string = ""
for ch in string:
    if ch.isupper() and idx == 0 or not ch.isupper():
        final_string += ch.lower()
    else:
        final_string += "_" + ch.lower()
    idx += 1
print(final_string)
