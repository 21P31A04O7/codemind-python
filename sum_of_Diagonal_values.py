r,c=map(int,input().split())
mat=[]
for i in range(r):
    row=list(map(int,input().split()))
    mat.append(row)
diagonalsum=0
visited=set()
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1:
            if (i,j) not in visited:
                diagonalsum+=mat[i][j]
                visited.add((i,j))
print(diagonalsum)