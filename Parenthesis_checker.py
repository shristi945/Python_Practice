


string = '[()]{}{[()()]())}'
open = ['{','[','(']
close = ['}',']',')']
dict = {']':'[','}': '{',')': '('}
lis = []
flag = 0
for char in string:
    if char in open:
        lis.append(char)
    if char in close:
        last_ele = lis[-1]
        if last_ele is dict[char]:
            lis.pop()
        else:
            flag = 1
if flag == 1 :
    print("Not Balanced")
else:
    if len(lis) != 0:
        print("Not Balanced")
    else:
        print("Balanced")
