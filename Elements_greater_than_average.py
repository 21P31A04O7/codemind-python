n=int(input())
arr=list(map(int,input().split()))
avg=sum(arr)//n
count=0
for num in arr:
    if num>=avg:
        count+=1
print(count)