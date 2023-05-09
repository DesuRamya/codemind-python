def factor_sum(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s 
n=int(input())
m=int(input())
ns=factor_sum(n)
ms=factor_sum(m)
if ns==m and ms==n:
    print("Amicable")
else:
    print("Not Amicable")