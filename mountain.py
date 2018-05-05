def mntns(a = [[]]):
    mi = 0
    mj = 0
    mjj = 0
    for i in range(len(a)): 
        for j in range(len(a[i])):
            if a[i][j]>mj:
                mj=a[i][j]
                mi=i
                mjj = j
    return(mi,mjj)

row, colum = mntns([[1,2,3],[4,5,4],[3,2,1]])

print(row, colum)

            
