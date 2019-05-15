
string = "acaaabbbacdddd"
string = string+" "
u_list = [0]
counter = 0
for char in string:
    if char is not u_list[-1]:
        if len(u_list)>1 and counter!=0:
            ele = u_list.pop()
            print("popped:")
            print(ele, char)
            counter = 0

        u_list.append(char)
    elif char is u_list[-1]:
        counter += 1
if counter >1:
    ele = u_list.pop()
print(''.join(u_list[1:]))
print(u_list)
