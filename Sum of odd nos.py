## Given a range, calculate the sum of odd numbers in it

li=[]
t=0
for elem in range(1,20):
    if elem%2!=0:
        li.append(elem)
print(li)
for i in li:
    t=t+i
print(t)
