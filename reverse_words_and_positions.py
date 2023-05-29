s=input()
lst=list(s)
i=0
j=len(s)-1
while i<j:
    lst[i],lst[j]=lst[j],lst[i]
    i+=1
    j-=1
print(''.join(lst))