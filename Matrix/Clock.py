def mirrorImage(h,m):
    xh=0
    xm=0
    if (h>=1 and h<=10) and (m>=m and m<=59):
        xh=11-h
        xm=60-m
    elif(h>=11 and h<=12) and (m>=1 and m<=59):
        xh=23-h
        xm=60-m
    print(xh,':',xm)
    
while 1:
    h=int(input('enter the hours:'))
    m=int(input('enter the min:'))
    mirrorImage(h,m)
    x=int(input())
    if x==1:
        break
    else:
        continue
   

            
