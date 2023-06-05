num=int(input())
square=pow(num,2)
mod=pow(10,len(str(num)))
if square%mod==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")