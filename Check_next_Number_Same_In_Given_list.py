'''Write a python function which accepts a list of numbers and returns true if the list contains a 2 next to a 2.
Otherwise it should return false.
Sample Input1:
[1,2,1,2,3,4,5,2,2]
Exceptedd Output:
True
Sample Input2:
[3,2,5,1,2,1,2]
Excepted Output
False'''

def check_22(num_list):
    for i in range(len(num_list)-1):
        if num_list[i]==num_list[i+1]:
            return True
    return False
list1=[1,2,3,4,2,2,8,9]
list2=[1,2,3,4,5,6]
print(check_22(list1),'list one')
print(check_22(list2),'list two')
