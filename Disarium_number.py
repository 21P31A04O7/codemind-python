num=int(input())
num_digits=len(str(num))
temp=num
sum_digits=0
while temp>0:
    digit=temp%10
    sum_digits+=digit**num_digits
    temp//=10
    num_digits-=1
if sum_digits==num:
    print("True")
else:
    print("False")