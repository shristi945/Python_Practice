
from itertools import permutations

string = "ABDG"
plist = permutations(string)
for ele in plist:
    print("".join(ele))
