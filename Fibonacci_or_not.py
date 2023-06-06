n=int(input())
c=0
n1=0
n2=1
l=[]
while c<=n:
    n3=n1+n2
    c=c+1
    l.append(n3)
    n1=n2
    n2=n3
if n in l:
    print(True)
else:
    print(False)