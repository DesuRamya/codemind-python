s=input()
s1=str.lower(s)
l=[]
for i in s1:
    if i not  in l and i!=' ':
        l.append(i)
l.sort()
for i in l:
    print(i,end='')