def counter(string):
    di = {}
    for char in string:
        if char not in di.keys():
            di[char] = 1
        if char in di:
            di[char] += 1
    return di

s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
d = counter(s1)
print(d)
