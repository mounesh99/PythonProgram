while 1:
    print('\nPress 1 for Addition of Two Matrix.\nPress 2 for Substraction of Two Matrx.\nPress 3 for Multiplication of Two Matrix.\n')
    take=int(input())
    if take==1:
        print("additon of matrix")
    if take==2:
        print("Substraction of Matrix")
    if take==3:
        print("Multiplication of Matrix")
    print('\nPress n for continue c for exit()')
    print('(c/n):')
    x=input()
    if x=='n':
        continue
    else:
        break
