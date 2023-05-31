for l in input().split():
    t=[]
    v='aeiou'
    for i in l:
        if i not in v:
            t.append(i)
    t.sort()
    x=[]
    for i in l:
        x.append(i)
    k=0
    a=[]
    for i in l:
        if i not in v:
            a.append(t[k])
            k+=1
        else:
            a.append(i)
    s=''
    for i in a:
        s+=i
    print(s,end=' ')