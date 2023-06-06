n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if i==0 or i==1:
        s+=1
if len(arr)==s:
    print("True")
else:
    print("False")