s=input()
s1=str.lower(s)
l={}
for i in s1:
    if i!=' ':
        if i in l:
            l[i]+=1
        else:
            l[i]=1
l1=[]
for k,v in l.items():
    if v==1:
        l1.append(k)
l1.sort()
for i in l1:
    print(i,end='')