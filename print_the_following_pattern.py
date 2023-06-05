n=int(input())
for i in range(n):
    for j in range(i,n):
        print(chr(64+n-i),end=" ")
    print()