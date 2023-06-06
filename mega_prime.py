import math
def it(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
if it(n):
    while n:
        d=n%10
        n=n//10
        if d==2 or d==3 or d==5 or d==7:
            pass
        else:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")