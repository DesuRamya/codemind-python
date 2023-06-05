n=int(input())
a=[]
b=[] 
c=[]
for j in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for j in range(n):
    l=list(map(int,input().split()))
    b.append(l)
c=[[a[i][j]+b[i][j] for j in range(n)]for i in range(n)]
for i in c:
    for j in i:
        print(j,end=' ')
    print()