n=int(input())
s=0
k=0
if n<0:
    k=1
    n=abs(n)
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
if k==1:
    print("-"+str(s))
    exit()
print(s)