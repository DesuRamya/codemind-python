def fun(n):
    s=0
    r=0
    while n!=0:
        r=n%10
        n=n//10
        s=s+r
    return s
n=int(input())
while(n>9):
    n=fun(n)
print(n)