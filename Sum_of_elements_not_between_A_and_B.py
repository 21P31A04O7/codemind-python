n=int(input())
s=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(0,n):
    if l[i]<a or l[i]>b:
        s.append(l[i])
print(sum(s))