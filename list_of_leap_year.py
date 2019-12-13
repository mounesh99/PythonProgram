'''Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
Also write the pytest test cases to test the program.'''

def find_leap_year(given_year):
    count=0
    list_of_leap_year=[]
    while count<15:
        if(given_year%4==0 and given_year%100!=0) or (given_year%400==0):
            list_of_leap_year.append(given_year)
            count=count+1
        given_year=given_year+1
    return list_of_leap_year
list_of_leap_year=find_leap_year(2015)
print(list_of_leap_year)
