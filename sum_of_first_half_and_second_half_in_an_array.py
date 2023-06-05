n=int(input())
arr=list(map(int,input().split()))
f=0
s=0
for i in range(n):
    if i<n//2:
        f+=arr[i]
    else:
        s+=arr[i]
print(f)
print(s)