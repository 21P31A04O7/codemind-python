n=int(input().lower())
a=n*n
rev=0
rev2=0
while n!=0:
    rem=n%10
    n//=10
    rev=rev*10+rem
b=rev*rev
while b!=0:
    rem2=b%10
    b//=10
    rev2=rev2*10+rem2
if a==rev2:
    print("True")
else:
    print("False")