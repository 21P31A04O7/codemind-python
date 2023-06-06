def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
flog=0
for i in range(2,n):
    for j in range(2,n):
        if prime(i) and prime(j):
            if i<j:
                if i*j==n:
                    print(i,j)
                    flog=1
                    break
if flog!=1:
    print("-1")