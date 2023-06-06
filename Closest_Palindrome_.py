def sub(n):
    n=n-1
    while(n!=0):
        p=str(n)
        q=p[::-1]
        if p==q:
            return q
        else:
            n=n-1
def add(n):
    n=n+1
    while(n!=0):
        p=str(n)
        q=p[::-1]
        if p==q:
            return q
        else:
            n=n+1
n=int(input())
a=sub(n)
b=add(n)
if abs(n-int(a))<abs(n-int(b)):
    print(int(a))
elif abs(n-int(a))==abs(n-int(b)):
    print(a,b)
else:
    print(int(b))
