s1=input()
s2=input()
x1=str.lower(s1)
x2=str.lower(s2)
r1=list(x1.split())
r2=list(x2.split())
l=[]
for i in r2:
    if i in r1:
        if i not in l:
            l.append(i)
if len(l)==0:
    print(0)
else:
    for i in l:
        print(i,end=' ')