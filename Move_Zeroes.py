n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
for i in l:
    print(i,end=' ')