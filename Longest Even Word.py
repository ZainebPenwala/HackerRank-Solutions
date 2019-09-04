## Find the longest even word from the given string.

def lew(s):
    words=[elem for elem in s.split() if len(elem)%2==0]
    if len(words)==0:
        return 00
    else:
        max_elem=words[0]
        for elem in words:
            if len(elem)>len(max_elem):
                max_elem=elem
    return elem
print(lew("it is a pleasant day today"))
