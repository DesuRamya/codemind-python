n=int(input())
rev=0
i=1
temp=n
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==temp:
    print('Palindrome')
else:
    print('Not Palindrome')