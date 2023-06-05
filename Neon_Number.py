N=int(input())
sqr=N*N
sumofdigits=0
while sqr>0:
    sumofdigits=sumofdigits+sqr%10
    sqr=sqr//10
if(N==sumofdigits):
    print("Neon Number")
else:
    print("Not Neon Number")