n=int(input())
arr=list(map(int,input().split()))
decimal_value=0
for i in range(n):
    decimal_value+=arr[i]*(2**(n-i-1))
print(decimal_value)