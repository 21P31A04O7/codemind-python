n=int(input())
temp=n
rev=0
while n:
    r=n%10
    n=n//10
    rev=rev*10+r
if temp==rev:
    print("True")
else:
    print("False")