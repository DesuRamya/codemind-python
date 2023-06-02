s1=input()
s2=input()
x1=str.lower(s1)
x2=str.lower(s2)
l=[]
for i in x1:
    if i in x2:
        if i not in l and i!=' ':
            l.append(i)
l.sort()
if len(l)==0:
    print(-1)
else:
    for i in l:
        print(i,end='')