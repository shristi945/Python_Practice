
def rev_str (string):
    rev = string[::-1]
    return rev



string = "aaaabbaa"
sub = list(string[i:j+1] for i in range (len(string)) for j in range(i,len(string)))
pdict = {}
for ele in sub :
    if ele == rev_str(ele):
        pdict[ele]=len(ele)

v_list = list(pdict.values())
k_list = list(pdict.keys())
print(k_list[v_list.index(max(v_list))])
