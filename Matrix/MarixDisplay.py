def createNXNMatrix():
    m=int(input('Enter The Number of Row:'))
    n=int(input('enter The Number of Column:'))
    Mat=[]
    for i in range(0,m):
        Mat.append([])
    for i in range(0,m):
        for j in range(0,n):
            Mat[i].append(j)
            Mat[i][j]=0
    for i in range(0,m):
        for j in range(0,n):
            print('enter int Row',i+1,'Colum',j+1)
            Mat[i][j]=int(input())
    return Mat
l=createNXNMatrix()
print(l)
