def np(x):
    for i in range(2,x):
        if x%i==0:
            return True
    else:
        return False
x=int(input())
c=0
for i in range(1,x+1):
    if x%i==0:
        if np(i):
            c=c+1
print(c+1)