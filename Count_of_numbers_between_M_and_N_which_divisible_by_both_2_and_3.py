n,m=map(int,input().split())
c=0
for i in range(n,m+1):
    if i%6==0:
        c=c+1
print(c)