n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s and l.count(i)==i:
        s.append(i)
print(len(s))