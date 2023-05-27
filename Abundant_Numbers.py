n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
        a=sum(l)
if a>n:
    print("True")
else:
    print("False")