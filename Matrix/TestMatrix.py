#Method for Creating NXN matrix
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

#Method for Creating Resultant Matrix
def resultMatrix():
    if take==3:
        m=len(Mat1)
        n=len(Mat2[0])
    else:
        m=len(Mat1)
        n=len(Mat2)
    Mat=[]
    for i in range(0,m):
        Mat.append([])
    for i in range(0,m):
        for j in range(0,n):
            Mat[i].append(j)
            Mat[i][j]=0
    return Mat

#Method for Multiplication of Two Matrix
def Mul(Mat1,Mat2):
    ResMat=resultMatrix()
    for p in range(len(Mat1)):
        for q in range(len(Mat2[0])):
            for r in range(len(Mat2)):
                ResMat[p][q]+=Mat1[p][r]*Mat2[r][q]
    return ResMat

#Method for Addition of Two Matrix
def Add(Mat1,Mat2):
    ResMat=resultMatrix()
    for i in range(len(Mat1)):
        for j in range(len(Mat1[0])):
            ResMat[i][j]=Mat1[i][j]+Mat2[i][j]
    return ResMat

#Method for Substraction of Two Matrix
def Sub(Mat1,Mat2):
    ResMat=resultMatrix()
    for i in range(len(Mat1)):
        for j in range(len(Mat1[0])):
            ResMat[i][j]=Mat1[i][j]-Mat2[i][j]
    return ResMat
#Method for Display resultant Matrix
def display():
    print('Mttrix One:\n')
    for outer in Mat1:
        for inner in outer:
            print(inner,end=' ')
        print()
    print('Matrix Two:\n')
    for outer in Mat2:
        for inner in outer:
            print(inner,end=' ')
        print()
    print('"Resultant Matrix!"')
    for outer in ResultMatrix:
        for inner in outer:
            print(inner,end=' ')
        print()
#----------------------------------------------------
while 1:
    print('\nPress 1 for Addition of Two Matrix.\nPress 2 for Substraction of Two Matrx.\nPress 3 for Multiplication of Two Matrix.\n')
    take=int(input())
    
    if take==1:
        print('"Additional of Matrix"')
        print('"Enter the Matrix One"')
        Mat1=createNXNMatrix()
        print('"Enter the Second Matrix"')
        Mat2=createNXNMatrix()
        ResultMatrix=Add(Mat1,Mat2)
        display()
        
    if take==2:
        print('"Substraction of Matrix"')
        print('"Enter the Matrix One"')
        Mat1=createNXNMatrix()
        print('"Enter the Second Matrix"')
        Mat2=createNXNMatrix()
        ResultMatrix=Sub(Mat1,Mat2)
        display()
        
    if take==3:
        print('"Multiplication of Two Matrix"')
        print('"Enter the Matrix One"')
        Mat1=createNXNMatrix()
        print('"Enter the Matrix Two"')
        Mat2=createNXNMatrix()
        ResultMatrix=Mul(Mat1,Mat2)
        display()
        
        
    print('\nPress n for continue c for exit()')
    print('(n/c):')
    x=input()
    if x=='n':
        continue
    else:
        break




