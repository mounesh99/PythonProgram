st=input("enter the string:")
l=len(st)
for i in range(l//2,0,-1):
    prefix=st[0:i]
    sufix=st[l-i:l]
    if(prefix==sufix):
        print(i)
