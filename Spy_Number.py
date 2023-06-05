n=int(input())
sum=0
product=1
n1=n#112
while n>0:
    d=n%10#4
    sum=sum+d#6
    product=product*d#4
    n=n//10
if sum==product:
    print("Spy Number")
else:
    print("Not Spy Number")