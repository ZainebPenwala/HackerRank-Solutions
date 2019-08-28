## Find the  total number of pair of socks from the given array where n = elements in the array 

def sock (n,arr):
    c=0
    arr.sort()
    arr.append('#')
    i=0
    while i < n:
        if arr[i]==arr[i+1]:
            c=c+1
            i+=2
        else:
            i+=1
    return c
print(sock(10,[1,1,3,1,2,1,3,3,3,3]))
