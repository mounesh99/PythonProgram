#Write a python program to generate and display the next date of a given date.
def generate_next_date(day,month,year):
    leap_year=False
    if year%4==0 or year%100!=0 and year%400==0:
        leap_year=True
    else:
        leap_year=False
    if month==2 and day<29:
        if leap_year:
            day+=1
            month=month
            year=year
        else:
            day=1
            month=3
            year=year
    if month in [1,3,5,7,8,10,12]:
        if day==31 and month==12:
            day=1
            month=1
            year+=1
        elif day<31 and month<12:
            day=day+1
            month=month
            year=year
        elif day==31 and month<12:
            day=1
            month+=1
            year=year
    else:
        if day==30:
            day=1
            month+=1
            year=year
        else:
            if month!=2:
                day+=1
                month=month
                year=year
    print(day,"-",month,"-",year)
while 1:
    day=int(input('enter the day:'))
    month=int(input('enter the month:'))
    year=int(input('enter the year:'))
    generate_next_date(day,month,year)
    x=input('enter the n for continue and c for exit()')
    if x=='n':
        continue
    else:
        break
